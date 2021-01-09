"""chatApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views as base_views


from accounts import urls as accounts_urls
from chat import urls as chat_urls
from machine import urls as makina
from genel import urls as genel_urls
from front import urls as front_urls
from backend import urls as backend_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_views.HomePage.as_view(), name='home'),
    path('accounts/', include(accounts_urls)),
    path('chat/', include(chat_urls)),
    path('machine/',include(makina)),
    path('genel/',include(genel_urls)),
    path('front/',include(front_urls)),
    path('backend/',include(backend_urls)),


]
