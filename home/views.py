from django.shortcuts import render
from . models import Fixture


def home(request):
    fixtures = Fixture.objects.all()
    return render(request, "home/home.html", {"fixtures": fixtures})

def about(request):
    return render(request, "home/about.html" )

def fans(request):
    return render(request, "home/fans.html" )