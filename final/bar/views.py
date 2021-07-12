from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import *


def base(request):
    return render(request, 'bar/home.html')


def overview(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
        'message': '居酒屋情報',
        'articles': articles,
        'searchForm': searchForm,
    }
    return render(request, 'bar/overview.html', context)



def detail(request, id):
    articles = get_object_or_404(Article, pk=id)
    context = {
        'message': '情報' + str(id),
        'articles': articles,
    }
    return render(request, 'bar/detail.html', context)



def new(request):
    articleForm = ArticleForm()

    context = {
        'message': 'New Article',
        'articleForm': articleForm,
    }
    return render(request, 'bar/new.html', context)


def create(request):
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            articles = articleForm.save()

    context = {
        'message': '居酒屋情報 追加' + str(articles.id),
        'articles': articles,
    }
    return render(request, 'bar/detail.html', context)


def edit(request, id):
    articles = get_object_or_404(Article, pk=id)
    articleForm = ArticleForm(instance=articles)

    context = {
        'message': 'Edit Article',
        'articles': articles,
        'articleForm': articleForm,
    }
    return render(request, 'bar/edit.html', context)


def update(request, id):
    if request.method == 'POST':
        articles = get_object_or_404(Article, pk=id)
        articleForm = ArticleForm(request.POST, instance=articles)
        if articleForm.is_valid():
            articleForm.save()
    
    context = {
        'message': 'Update article' + str(id),
        'articles': articles,
    }
    return render(request, 'bar/detail.html', context)


def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    articles = Article.objects.all()
    context = {
        'message': 'Delete Article' + str(id),
        'articles': articles,
    }
    return render(request, 'bar/overview.html', context)