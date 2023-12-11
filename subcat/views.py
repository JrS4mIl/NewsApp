from django.shortcuts import render,redirect
from .models import SubCat
from django.contrib import messages
from cat.models import Category
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def subcat_list(request):
    subcat=SubCat.objects.all()
    context={
        'subcat':subcat
    }

    return  render(request,'back/subcat_list.html',context)

@login_required(login_url='login')
def subcat_add(request):
    cat=Category.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        catid=request.POST.get('cat')
        if name=='':
            messages.error(request,'Category bos gecmeyiniz')
            return redirect('subcat_add')
        if len(SubCat.objects.filter(name=name))!=0:
            messages.error(request,'Bu category zaten mevcut')
            return redirect('subcat_add')
        catname=Category.objects.get(pk=catid).name
        b=SubCat(name=name,catname=catname,catid=catid)
        b.save()
        messages.success(request,'Basariyla Eklediniz')
        return redirect('subcat_list')

    context={
        'cat':cat
    }
    return  render(request,'back/subcat_add.html',context)