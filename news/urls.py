from django.urls import path
from . import views

urlpatterns = [
    path('news/<slug:slug>',views.news_detail,name='detail')

]
