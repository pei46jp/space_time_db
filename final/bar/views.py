from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm


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
    return HttpResponse('This is new.')


def create(request):
    article = Article(content='居酒屋名', user_name='my')
    article.save()

    articles = Article.objects.all()
    context = {
        'message': '居酒屋情報 追加',
        'articles': articles,
    }
    return render(request, 'bar/overview.html', context)


def edit(request, id):
    return HttpResponse('This is edit ' + str(id))


def update(request, id):
    return HttpResponse('This is update ' + str(id))


def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    articles = Article.objects.all()
    context = {
        'message': 'Delete Article' + str(id),
        'articles': articles,
    }
    return render(request, 'bar/overview.html', context)