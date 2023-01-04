"""wash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from . import views

urlpatterns = [
    path('', views.wash1, name='wash1'),
    path('templates/wash4', views.wash4, name='wash4'),
    path('templates/wash3', views.wash3, name='wash3'),
    path('templates/wash2', views.wash2, name='wash2'),
    path('../home/', views.index, name='index'),
    path('../../home/', views.index, name='index2'),

]