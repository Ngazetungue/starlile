from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import NewsForm
from . models import Fixture, News


def home(request):
    fixtures = Fixture.objects.all()
    return render(request, "home/home.html", {"fixtures": fixtures})

def about(request):
    return render(request, "home/about.html" )

def fans(request):
    return render(request, "home/fans.html" )

def news_list(request):
    news = News.objects.all()
    return render(request, 'home/news_list.html', {'news': news})

def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'home/news_detail.html', {'news': news_item})

def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'home/news_form.html', {'form': form})

def news_update(request, id):
    news_item = get_object_or_404(News, id=id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news_item)
    return render(request, 'home/news_form.html', {'form': form})

def news_delete(request, id):
    news_item = get_object_or_404(News, id=id)
    if request.method == 'POST':
        news_item.delete()
        return redirect('news_list')
    return render(request, 'home/news_confirm_delete.html', {'news': news_item})
