from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def new(request):
    return render(request, 'posts/new.html')

@login_required
def create(request):
    # title = request.GET.get('title')
    # content = request.GET.get('content')

    # post = Article(title=title, content=content)
    # article.save()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('posts:index') #, article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def delete(request, num):
    pass


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'posts/index.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'posts/detail.html', context)

@login_required
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('posts:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('posts:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'posts/update.html', context)
