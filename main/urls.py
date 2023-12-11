
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('panel/',views.panel,name='panel'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),


]
