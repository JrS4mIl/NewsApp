from django.shortcuts import render,redirect
from .models import Category
from django.contrib import messages
# Create your views here.
def cat_list(request):
    cat=Category.objects.all()
    context={
        'cat':cat
    }

    return  render(request,'back/cat_list.html',context)


def cat_add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        if name=='':
            messages.error(request,'Category bos gecmeyiniz')
            return redirect('add_cat')
        if len(Category.objects.filter(name=name))!=0:
            messages.error(request,'Bu category zaten mevcut')
            return redirect('add_cat')

        else:
            data=Category(name=name)
            data.save()
            messages.success(request,'Category Basariyla Eklendi')

            return redirect('cat_list')



    return  render(request,'back/add_cat.html')