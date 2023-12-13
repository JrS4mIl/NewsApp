
from django.urls import path
from . import views

urlpatterns = [
    path('contact/submit/',views.contact_add,name='contact_add'),
    path('panel/contactlist', views.contact_list, name='contactlist'),
    path('panel/contactlist/del/<int:pk>/', views.contact_del, name='contactdel'),


]
