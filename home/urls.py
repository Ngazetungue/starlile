from django.urls import path
from . views import home, about, team, fans, matches, store, news_list, news_detail, news_create, news_update, news_delete

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("team/", team, name="team"),
    path("fans/", fans, name="fans"),
    path("matches/", matches, name="matches"),
    path("store/", store, name="store"),

    path('news/', news_list, name='news_list'),
    path('news/<int:id>/', news_detail, name='news_detail'),
    path('news/create/', news_create, name='news_create'),
    path('news/update/<int:id>/', news_update, name='news_update'),
    path('news/delete/<int:id>/', news_delete, name='news_delete'),


]
