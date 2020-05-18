"""hello3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from pervoe import views



urlpatterns = [   
    path('', views.index),
    path('create', views.create),
    path('film', views.film),
    path('bilet', views.bilet),
    path('bilet/<int:idfilm>/', views.bilet),
    path('log', views.log),
    path('lk', views.lk),
    path('pokupka', views.pokupka),
    path('logout1', views.logout1),
    re_path(r'^film/(?P<page>\d+)/', views.film),
    re_path(r'^bilet/\d+/', views.bilet),
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    path('searchlist', views.searchlist),
    path('contact', views.contact),
    re_path('\w+', views.page404),
]
