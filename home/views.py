from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import NewsForm
from . models import Fixture, Result, Player,  News
from django.http import Http404
from .models import Fixture
import calendar
from datetime import datetime
from django.utils import timezone


def home(request):
    fixtures = Fixture.objects.order_by("-date")[:3]
    results = Result.objects.order_by('-date')[:3]
    players = Player.objects.all()[:4]
    return render(request, "home/home.html", {"fixtures": fixtures,"results": results, "players": players})

def about(request):
    return render(request, "home/about.html" )

def team(request):
    forwards = Player.objects.filter(position='FWD')
    midfielders = Player.objects.filter(position='MID')
    defenders = Player.objects.filter(position='DEF')
    goalkeepers = Player.objects.filter(position='GK')
    
    context = {
        'forwards': forwards,
        'midfielders': midfielders,
        'defenders': defenders,
        'goalkeepers': goalkeepers,
    }
    
    return render(request, "home/squad.html", context)


def fans(request):
    return render(request, "home/fans.html" )


def matches(request):
    current_year = timezone.now().year
    current_month = timezone.now().month

    selected_month = request.GET.get('month', 'August') 
    selected_year = int(request.GET.get('year', current_year)) 

    valid_months = {
        'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12,
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5
    }

    if selected_month not in valid_months:
        selected_month = 'August'

    month_number = valid_months[selected_month]
    if month_number in range(8, 13): 
        fixtures = Fixture.objects.filter(date__month=month_number, date__year=selected_year)
    else: 
        fixtures = Fixture.objects.filter(date__month=month_number, date__year=selected_year + 1)

    context = {
        "month": selected_month,
        "year": selected_year,
        "fixtures": fixtures,
        "valid_months": list(valid_months.keys()),
    }

    return render(request, "home/matches.html", context)

def store(request):
    return render(request, "home/store.html" )

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
