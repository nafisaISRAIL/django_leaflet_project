from django.shortcuts import render
from datetime import datetime, timedelta
from master.scraping.models import Article, Category
from master.scraping.forms import DateFilterForm
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

import decimal
import json

# Create your views here.


def posts(request):
    articles = Article.objects.all()
    return render(request, 'scraping/index.html', {'articles': articles})


def map_view(request):
    delta = datetime.now() - timedelta(days=1)
    form = DateFilterForm(request.POST or None)
    date = None
    if form.is_valid():
        date = form.cleaned_data.get('filter_by')
        if date == 'week':
            delta = datetime.now() - timedelta(days=7)
        elif date == 'month':
            delta = datetime.now() - timedelta(days=30)

    filter_cat = request.GET.getlist('category', [])
    categories = Category.objects.all()
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


def new_map(request):
    delta = datetime.now() - timedelta(days=1)
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
    filter_cat = [int(x) for x in filter_cat]
    articles = list(map(lambda x: str(x) if isinstance(
        x, decimal.Decimal) else x, articles))
    #articles = json.dumps(list(articles), cls=DjangoJSONEncoder)

    return JsonResponse(articles, safe=False)
