from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

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
           return render(request, 'back/add_news.html')
        try:
            myfile=request.FILES['myfile']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            url=fs.url(filename)

            if str(myfile.content_type).startswith('image'):
                if myfile.size<5000000:

                    data = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date="2023", picname=filename,
                                picurl=url, writer='.', catname=newscat, catid=0, show=0)
                    data.save()
                    messages.success(request, 'News Added')
                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    messages.error(request, 'Resim Dosyasi Cok buyuk en fazla 5 MB')
                    return redirect('add_news')

            else:
                fs=FileSystemStorage()
                fs.delete(filename)
                messages.error(request,'Lutfen Resim Formatinda dosya seciniz')
                return redirect('add_news')


        except:
            messages.error(request, 'Lutfen Image Alanini Bos gecmeyelim')
            return redirect('add_news')

    return render(request, 'back/add_news.html')

def news_delete(request,pk):
    try:
        b=News.objects.get(pk=pk)
        fs=FileSystemStorage()
        fs.delete(b.picname)
        b.delete()
    except:
        messages.error(request,'Somting Wrong')

    return redirect('news_list')