from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
from django.contrib import messages


# Create your views here.
def news_detail(request, slug):
    news = News.objects.filter(slug=slug)
    site = Main.objects.get(pk=1)

    context = {
        'site': site,
        'news': news
    }
    return render(request, 'news/detail.html', context)


def news_list(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'back/news_list.html', context)


def add_news(request):
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat=request.POST.get('newscat')
        newstxtshort=request.POST.get('newstxtshort')
        newstxt=request.POST.get('newstxt')

        if newstitle=="" or newstxt=="" or newstxtshort=="" or newstxt=="" or newscat=="":
           messages.error(request,'Bos Gecilmez')

        data=News(name=newstitle,short_txt=newstxtshort,body_txt=newstxt,date="2023",pic='1.png',writer='.',catname=newscat,catid=0,show=0)
        data.save()
        messages.success(request,'News Added')
        return redirect('news_list')

    return render(request, 'back/add_news.html')
