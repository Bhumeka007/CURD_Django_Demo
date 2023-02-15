from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = NewsForm()
    return render(request, 'home.html', {'form': form})



def news_update(request, pk):
    news = News.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = NewsForm(instance=news)
    return render(request, 'home.html', {'form': form})

def news_delete(request, pk):
    if request.method == 'POST':
        News.objects.get(pk=pk).delete()
        return redirect('articles')
    else:
        news = News.objects.get(pk=pk)
        return render(request, 'deleteNews.html', {'news': news})



def articles(request):
    articles = News.objects.all()
    return render(request, 'articles.html', {'articles': articles})
