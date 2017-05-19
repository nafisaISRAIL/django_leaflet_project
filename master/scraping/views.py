from django.shortcuts import render
from master.scraping.models import Article

# Create your views here.


def posts(request):
    articles = Article.objects.all()
    return render(request, 'scraping/index.html', {'articles': articles})


def map_view(request):
    footer = Article.objects.filter(category__name='pedestrian')
    crash = Article.objects.filter(category__name='crash')
    bump = Article.objects.filter(category__name='bump')
    context = {
        'footer': footer,
        'crash': crash,
        'bump': bump
    }
    return render(request, 'scraping/map.html', context)

