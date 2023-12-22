"""
URL configuration for newsApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from main.sitemap import MyNewsSiteMap
sitemaps={
    'news':MyNewsSiteMap(),
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap\.xml',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('',include('main.urls')),
    path('',include('news.urls')),
    path('',include('cat.urls')),
    path('',include('subcat.urls')),
    path('',include('contactform.urls')),
    path('', include('manager.urls')),
    path('', include('blacklist.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)