from django.db.models import Count
from django.shortcuts import render
from datetime import datetime, timedelta
from master.scraping.models import Article, Category
from django.shortcuts import get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

import decimal
import json

# Create your views here.


def posts(request):
    articles = Article.objects.all().order_by('-id')
    return render(request, 'scraping/index.html', {'articles': articles})


def map_view(request):
    delta = datetime.now() - timedelta(days=0)
    filter_cat = request.GET.getlist('category', [])
    select_date = request.GET.get('filter_by')
    if select_date == 'week':
        delta = datetime.now() - timedelta(days=7)
    elif select_date == 'month':
        delta = datetime.now() - timedelta(days=30)
    articles = Article.objects.values_list(
        'id',
        'latitude',
        'longitude',
        'title',
        'url',
        'category').filter(
        created_at__gte=delta,
        latitude__isnull=False,
        longitude__isnull=False)
    if len(filter_cat):
        articles = articles.filter(category__id__in=filter_cat)

    if request.is_ajax():
        articles = list(map(lambda x: str(x) if isinstance(
            x, decimal.Decimal) else x, articles))
        return JsonResponse(articles, safe=False)

    categories = Category.objects.all()
    filter_cat = [int(x) for x in filter_cat]

    articles = json.dumps(list(articles), cls=DjangoJSONEncoder)
    return render(request, 'scraping/map.html', {'data': articles,
                                                 'categories': categories,
                                                 'filter_cat': filter_cat,
                                                 })


def by_category(request, id):
    category = get_object_or_404(Category, pk=id)
    articles = Article.objects.filter(category=category).order_by('-id')
    count = articles.count()
    return render(request, 'scraping/by_category.html', locals())


def select_category(request):
    categories = Category.objects.annotate(count_articles=Count(
        'article')).all()
    return render(request, 'scraping/select_category.html', locals())


def detail_article(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'scraping/detail_article.html',
                  {'article': article})
