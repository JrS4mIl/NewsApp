from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Category
from django.contrib import messages
import csv
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='login')
def cat_list(request):
    cat = Category.objects.all()
    context = {
        'cat': cat
    }

    return render(request, 'back/cat_list.html', context)


@login_required(login_url='login')
def cat_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name == '':
            messages.error(request, 'Category bos gecmeyiniz')
            return redirect('add_cat')
        if len(Category.objects.filter(name=name)) != 0:
            messages.error(request, 'Bu category zaten mevcut')
            return redirect('add_cat')

        else:
            data = Category(name=name)
            data.save()
            messages.success(request, 'Category Basariyla Eklendi')

            return redirect('cat_list')

    return render(request, 'back/add_cat.html')


def export_cat_csv(request):
    response = HttpResponse(content_type='text/csv')

    response['Content_Disposition'] = "attachment;filname='cat.csv'"
    writer = csv.writer(response)
    writer.writerow(['Title', 'Count'])
    for i in Category.objects.all():
        writer.writerow([i.name, i.count])
    return response


def import_cat_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'CSV forma dosya yukleyiniz')
        if csv_file.multiple_chunks():
            messages.error(request,'File too Larg')

        file_data = csv_file.read().decode('utf-8')
        lines = file_data.split('\n')
        for line in lines:
            fields = line.split(',')
            try:
                if len(Category.objects.filter(name=fields[0])) == 0 and fields[0] != "Title":
                    b = Category(name=fields[0])
                    b.save()

            except:
                print('finish')

    return redirect('cat_list')
