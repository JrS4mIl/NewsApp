from django.shortcuts import render,get_object_or_404,redirect
from .models import Main
from news.models import  News
# Create your views here.
def home(request):
    site=Main.objects.get(pk=1)
    news=News.objects.all()

    context={
        'site':site,
        'news':news
    }
    return render(request,'main/home.html',context)

def about(request):
    site = Main.objects.get(pk=1)

    context = {
        'site': site,
    }
    return render(request,'main/about.html',context)

def panel(request):
    return render(request,'back/index.html')