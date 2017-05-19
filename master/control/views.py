from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from master.scraping.models import Article
from master.control.forms import UpdateArticleForm, DeleteAtricleForm


def is_anonymous(func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated():
            return redirect(settings.REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper


@is_anonymous
def singin(request):
    form = AuthenticationForm(request, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('articles-list')
    return render(request, 'control/login.html', locals())


@login_required
def singout(request):
    logout(request)
    return redirect('main')


def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'control/articles_list.html',
                  {'articles': articles})


def update_article(request, pk):
    article = Article.objects.get(pk=pk)
    form = UpdateArticleForm(request.POST or None,
                             instance=article)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('articles-list'))
    return render(request, 'control/update_article.html', locals())


def detail_article(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'control/detail_article.html',
                  {'article': article})


@require_POST
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect(reverse('articles-list'))

