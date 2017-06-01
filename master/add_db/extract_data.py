from urllib.request import urlopen
from bs4 import BeautifulSoup
import Stemmer
from datetime import datetime
import locale
import pymorphy2

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


class Crawler(object):
    def __init__(self, url, *args):  # all links from db, global variable
        self.args = list(args)
        self.url = url
        self.bsObj = BeautifulSoup(urlopen(self.url), 'html.parser')

    def internallinks(self):
        divs = self.bsObj.find('div', {'class': 'row lineNews'}
                               ).findAll('div', {'class': 'one'})
        new_links = []

        for div in divs:
            link = div.find('a')
            format_link = 'http://24.kg{}'.format(link.attrs['href'])
            if format_link not in self.args:
                new_links.append(format_link)
        return new_links


class Scraper(object):
    def __init__(self, url, *words):
        self.url = url
        self.words = words
        self.obj = BeautifulSoup(urlopen(self.url), 'html.parser')

    def get_post(self):
        post = []
        today = datetime.now()
        date = datetime.strftime(today, '%Y-%m-%d')
        if date == str(self.get_date()):
            text = self.get_text()
            if text is not None:
                post.append(self.get_title())
                post.append(self.get_time())
                post.append(str(self.get_date()))
                post.append(text)
                post.append(self.get_url())
                return post
        return None

    def get_url(self):
        return self.url

    def get_date(self):
        bsObj = self.obj
        date_string = bsObj.find(
            'div', {'class': 'col-xs-12 newsDate hidden-sm hidden-md hidden-lg'
                    }).get_text().split(',')
        date_post = date_string[1].split()

        morph = pymorphy2.MorphAnalyzer()

        month = morph.parse(date_post[1])[0].inflect({'sing', 'nomn'}).word
        date_new = '{} {} {}'.format(
            date_post[0], month.capitalize(), date_post[2])
        date = datetime.date(datetime.strptime(date_new, '%d %B %Y'))

        return date

    def get_time(self):
        bsObj = self.obj
        date_string = bsObj.find(
            'div', {'class': 'col-xs-12 newsDate hidden-sm hidden-md hidden-lg'
                    }).get_text().split(',')
        post_time = date_string[0]
        return post_time

    def get_title(self):
        bsObj = self.obj
        title = bsObj.find('h1', {'class': 'newsTitle'}).get_text()
        return title

    def get_text(self):
        bsObj = self.obj
        data = []
        for i in bsObj.find('div',
                            {'class': 'js-mediator-article'}).findAll('p'):
            data.append(i.get_text())
        data = ''.join(data)
        count = 0
        stemmed_data = Stemmer.Stemmer('russian')
        for i in stemmed_data.stemWords(data.split()):
            if i in self.words:
                count += 1
        if count > 2:
            return data
        return None
