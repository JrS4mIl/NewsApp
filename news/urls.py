from django.urls import path
from . import views

urlpatterns = [
    path('news/<slug:slug>',views.news_detail,name='detail'),
    path('panel/news/list',views.news_list,name='news_list'),
    path('panel/news/add', views.add_news, name='add_news'),

]
