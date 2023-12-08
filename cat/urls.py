from django.urls import path
from . import views

urlpatterns = [
    path('panel/category/list',views.cat_list,name='cat_list'),
    path('panel/category/add',views.cat_add,name='add_cat')

]