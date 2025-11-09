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
    article = Article.objects.get(pk=num)
    article.delete()
    return redirect('posts:index')


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'posts/index.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
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

@login_required
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('posts:detail', article.pk)
    # else
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)