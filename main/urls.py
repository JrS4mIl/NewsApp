
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/', views.contact, name='contact'),
    path('panel/',views.panel,name='panel'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('panel/settings',views.site_settings,name='site_settings'),
    path('panel/about/settings',views.about_settings,name='about_settings'),
    path('panel/change/pass', views.change_password, name='change_pass'),

]
