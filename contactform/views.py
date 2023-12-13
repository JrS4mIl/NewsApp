from django.shortcuts import render,redirect
from .models import ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def contact_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        txt = request.POST.get('msg')
        if name == "" or email == "" or txt == "":
            messages.error(request, 'Alanlari Bos gecmeyiniz')
        else:
            d = ContactForm(name=name, email=email, txt=txt)
            d.save()
            messages.success(request, 'Tesekkur Ederiz!! Mesajiniz Iletildi')
            return redirect('contact')
        return redirect('contact')
@login_required(login_url='login')
def contact_list(request):
    contactform=ContactForm.objects.all()
    context={
        'contactform':contactform
    }
    return render(request,'back/contactlist.html',context)

@login_required(login_url='login',)
def contact_del(request,pk):
    b=ContactForm.objects.filter(pk=pk)
    b.delete()
    messages.error(request,'Silindi')
    return redirect('contactlist')