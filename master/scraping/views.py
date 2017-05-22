from django.shortcuts import render
from datetime import datetime, timedelta
from master.scraping.models import Article, Category
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

import json

# Create your views here.


def posts(request):
    articles = Article.objects.all()
    return render(request, 'scraping/index.html', {'articles': articles})


def map_view(request):
    filter_cat = request.GET.getlist('category', [])
    categories = Category.objects.all()
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
    filter_cat = [int(x) for x in filter_cat]

    articles = json.dumps(list(articles), cls=DjangoJSONEncoder)
    return render(request, 'scraping/map.html', {'data': articles,
                                                 'categories': categories,
                                                 'filter_cat': filter_cat,
                                                 })
