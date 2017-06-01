from django.core.management.base import BaseCommand
from master.add_db.extract_data import Crawler, Scraper
from master.scraping.models import Article
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        links = list(Article.objects.all().values_list(
        'url', flat=True))  # all links from db

        words = ['Бишкек', 'ДТП', 'жертв',
                 'пешеход', 'автокатастроф',
                 'автомашин', 'сбил', 'водител',
                 'погибш', 'переход', 'дорог', 'наезд',
                 'машин', 'авто', 'сбив', 'протаран']

        crawler = Crawler(settings.MAIN_URL, *links)
        new_links = crawler.internallinks()

        for link in new_links:
            post = Scraper(link, *words)
            p = post.get_post()
            if p is not None:
                link = p[4]
                title = p[0]
                time = p[1]
                date = p[2]
                text = p[3]
                article = Article(title=title, article_time=time,
                                  article_date=date, text=text, url=link)
                article.save()
