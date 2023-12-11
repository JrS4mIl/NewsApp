from django.shortcuts import render,get_object_or_404,redirect
from .models import Main
from news.models import  News
# Create your views here.
from cat.models import Category
from subcat.models import SubCat
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages, auth
def home(request):
    site=Main.objects.get(pk=1)
    news=News.objects.all().order_by('-created_date')
    cat=Category.objects.all()
    subcat=SubCat.objects.all()
    slider=News.objects.all().order_by('-created_date')[:3]



    context={
        'site':site,
        'news':news,
        'cat':cat,
        'subcat':subcat,
        'slider':slider

    }
    return render(request,'main/home.html',context)

def about(request):
    site = Main.objects.get(pk=1)

    context = {
        'site': site,
    }
    return render(request,'main/about.html',context)


@login_required(login_url='login')
def panel(request):
    return render(request,'back/index.html')

def login(requests):
    if requests.method=='POST':
        username=requests.POST.get('username')
        password=requests.POST.get('password')
        if username !="" and password !="":
            user=auth.authenticate(requests,username=username,password=password)
            if user != None:
                auth.login(requests, user)
                return redirect('panel')

    return render(requests,'back/login.html')

def logout(requests):
    if requests.method=='POST':
        auth.logout(requests)
        return redirect('home')
    messages.success(requests, 'You are loggen aut')
    return redirect('home')

def site_settings(request):
    return render(request,'back/settings.html')