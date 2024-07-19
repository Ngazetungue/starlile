from django.urls import path
from . views import home, about, fans

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("fans/", fans, name="fans"),
]
