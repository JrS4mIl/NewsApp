from django.shortcuts import render,redirect
from .models import Manager
from django.contrib import messages
from django.contrib.auth.models import Group,Permission
# Create your views here.
def manager_list(request):
    manager=Manager.objects.all()
    context={
        'manager':manager
    }
    return render(request,'back/manager_list.html',context)

def manager_delete(request,pk):
    manager=Manager.objects.get(pk=pk)
    manager.delete()
    messages.warning(request,'Kullanici silindi')


    return redirect('manager_list')

def manager_group(request):
    group=Group.objects.all()
    return render(request,'back/group.html',{'group':group})

