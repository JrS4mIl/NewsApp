from django.shortcuts import render,get_object_or_404,redirect
from .models import News
from main.models import Main
# Create your views here.
def news_detail(request,slug):
    news=News.objects.filter(slug=slug)
    site = Main.objects.get(pk=1)

    context={
        'site':site,
        'news':news
    }
    return render(request,'news/detail.html',context)