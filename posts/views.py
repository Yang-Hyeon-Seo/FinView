from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

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
