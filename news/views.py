from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from .models import News
from main.models import Main
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from subcat.models import SubCat
from cat.models import Category
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def news_detail(request, slug):
    news = News.objects.filter(slug=slug)
    site = Main.objects.get(pk=1)

    context = {
        'site': site,
        'news': news
    }
    return render(request, 'news/detail.html', context)

@login_required(login_url='login')
def news_list(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'back/news_list.html', context)


@login_required(login_url='login')
def add_news(request):
    subcat=SubCat.objects.all()
    context={
        'subcat':subcat
    }
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat=request.POST.get('newscat')
        newstxtshort=request.POST.get('newstxtshort')
        newstxt=request.POST.get('newstxt')
        newsid=request.POST.get('newscat')

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
                    newsname=SubCat.objects.get(pk=newsid).name
                    ocatid=SubCat.objects.get(pk=newsid).catid

                    b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date="2023", picname=filename,picurl=url, writer='.', catname=newsname, catid=newsid, show=0,ocatid=ocatid)
                    b.save()

                    count=len(News.objects.filter(ocatid=ocatid))
                    b.count=count
                    b.save()


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

    return render(request, 'back/add_news.html',context)
@login_required(login_url='login')
def news_delete(request,pk):
    try:
        b=News.objects.get(pk=pk)
        fs=FileSystemStorage()
        fs.delete(b.picname)
        ocatid = News.objects.get(pk=pk).ocatid
        b.delete()

        count = len(News.objects.filter(ocatid=ocatid))

        m = Category.objects.get(pk=ocatid)
        m.count = count
        b.save()
    except:
        messages.error(request,'Somting Wrong')

    return redirect('news_list')
@login_required(login_url='login')
def news_edit(request,pk):
    if len(News.objects.filter(pk=pk))==0:

        return render(request,'back/err.html')
    subcat=SubCat.objects.all()
    news=News.objects.get(pk=pk)
    context={
        'news':news,
        'pk':pk,
        'subcat':subcat,
    }
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat=request.POST.get('newscat')
        newstxtshort=request.POST.get('newstxtshort')
        newstxt=request.POST.get('newstxt')
        newsid=request.POST.get('newscat')

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
                    newsname=SubCat.objects.get(pk=newsid).name

                    data = News.objects.get(pk=pk)
                    fss = FileSystemStorage()
                    fss.delete(data.picname)
                    data.name=newstitle
                    data.short_txt=newstxtshort
                    data.body_txt=newstxt
                    data.picname=filename
                    data.picurl=url
                    data.catname=newsname
                    data.catid=newsid
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
            newsname = SubCat.objects.get(pk=newsid).name

            data = News.objects.get(pk=pk)

            data.name = newstitle
            data.short_txt = newstxtshort
            data.body_txt = newstxt

            data.catname = newsname
            data.catid = newsid
            data.save()
            messages.success(request, 'Update News')
            return redirect('news_list')

    return render(request,'back/news_edit.html',context)