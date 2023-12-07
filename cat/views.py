from django.shortcuts import render
from .models import Category
# Create your views here.
def cat_list(request):
    cat=Category.objects.all()
    context={
        'cat':cat
    }

    return  render(request,'back/cat_list.html',context)