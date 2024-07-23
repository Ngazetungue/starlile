from django.urls import path
from . views import home, about, fans, news_list, news_detail, news_create, news_update, news_delete

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("fans/", fans, name="fans"),
    

    path('news/', news_list, name='news_list'),
    path('news/<int:id>/', news_detail, name='news_detail'),
    path('news/create/', news_create, name='news_create'),
    path('news/update/<int:id>/', news_update, name='news_update'),
    path('news/delete/<int:id>/', news_delete, name='news_delete'),


]
