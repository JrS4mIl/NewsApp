from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
# Create your views here.
from cat.models import Category
from subcat.models import SubCat
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ipware import get_client_ip
from django.contrib import messages, auth
from ip2geotools.databases.noncommercial import DbIpCity
from zeep import  Client
import  requests
import json
from bs4 import BeautifulSoup

def home(request):
    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-created_date')
    cat = Category.objects.all()
    subcat = SubCat.objects.all()
    slider = News.objects.all().order_by('-created_date')[:3]
    popnews = News.objects.all().order_by('-show')[:3]

    context = {
        'site': site,
        'news': news,
        'cat': cat,
        'subcat': subcat,
        'slider': slider,
        'popnews': popnews

    }
    return render(request, 'main/home.html', context)


def about(request):
    popnews = News.objects.all().order_by('-show')[:3]
    site = Main.objects.get(pk=1)
    cat = Category.objects.all()

    context = {
        'site': site,
        'cat': cat,
        'popnews': popnews,
    }
    return render(request, 'main/about.html', context)


@login_required(login_url='login')
def panel(request):
    return render(request, 'back/index.html')


def login(requests):
    if requests.method == 'POST':
        username = requests.POST.get('username')
        password = requests.POST.get('password')
        if username != "" and password != "":
            user = auth.authenticate(requests, username=username, password=password)
            if user != None:
                auth.login(requests, user)
                return redirect('panel')

    return render(requests, 'back/login.html')


def logout(requests):
    if requests.method == 'POST':
        auth.logout(requests)
        return redirect('home')
    messages.success(requests, 'You are loggen aut')
    return redirect('home')


@login_required(login_url='login')
def site_settings(request):
    if request.method == "POST":
        name = request.POST.get('name')
        tell = request.POST.get('tell')
        fb = request.POST.get('fb')
        tw = request.POST.get('tw')
        yt = request.POST.get('yt')
        link = request.POST.get('link')
        txt = request.POST.get('txt')
        if fb == "": fb = "#"
        if tw == "": tw = "#"
        if yt == "": yt = "#"
        if link == "": link = "#"

        if name == '' or tell == '' or txt == '':
            messages.error(request, 'Field bos gecilmez')
        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            picurl = url
            picname = filename


        except:
            picurl = '-'
            picname = '-'

            try:
                myfile2 = request.FILES['myfile2']
                fs2 = FileSystemStorage()
                filename2 = fs2.save(myfile2.name, myfile2)
                url2 = fs2.url(filename2)
                picurl2 = url2
                picname2 = filename2


            except:
                picurl2 = "-"
                picname2 = "-"

            b = Main.objects.get(pk=1)
            b.name = name
            b.tell = tell
            b.fb = fb
            b.tw = tw
            b.yt = yt
            b.link = link
            b.about = txt
            if picurl != "-": b.picurl = picurl
            if picname != "-": b.picname = picname
            if picurl2 != "-":  b.picurl2 = picurl2
            if picname2 != "-": b.picname2 = picname2
            b.save()
            messages.success(request, 'Guncellendi')

    site = Main.objects.get(pk=1)
    context = {
        'site': site
    }
    return render(request, 'back/settings.html', context)


@login_required(login_url='login')
def about_settings(request):
    if request.method == 'POST':
        txt = request.POST.get('txt')
        if txt == "":
            messages.error(request, 'Text Alanini Bos Gecmeyiniz')

        b = Main.objects.get(pk=1)
        b.abouttxt = txt
        b.save()
        messages.success(request, 'Guncellendi')
    context = {
        'about': about
    }

    return render(request, 'back/about_settings.html', context)


def contact(request):
    popnews = News.objects.all().order_by('-show')[:3]
    subcat = SubCat.objects.all()
    cat = Category.objects.all()
    site = Main.objects.get(pk=1)
    context = {
        'site': site,
        'popnews': popnews,
        'cat': cat,
        'subcat': subcat
    }

    return render(request, 'main/contact.html', context)


def change_password(request):
    if request.method == 'POST':
        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')
        if oldpass == "" and newpass == "":
            messages.error(request, 'Alanlari bos gecmeyiniz')
        user = authenticate(username=request.user, password=oldpass)
        if user != None:
            if len(newpass) < 8:
                messages.error(request, 'Sifreniz 8 karekterden az olmamamli')
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            for i in newpass:
                if i > "0" and i < "9":
                    count1 = 1
                if i > "A" and i < "Z":
                    count2 = 1
                if i > "a" and i < "z":
                    count3 = 1
                if i > "!" and i < "(":
                    count4 = 1
            if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1:
                user = User.objects.get(username=request.user)
                user.set_password(newpass)
                user.save()
                return redirect('logout')

        else:
            messages.error(request, 'your password not Correct')

    return render(request, 'back/changepass.html')
