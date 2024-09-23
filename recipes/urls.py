"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import HttpResponse
from recipes.views import home, contato, sobre

# HTTP request
def _home(request):
    return HttpResponse('<h1>Hello Word</h1>')

def _sobre(request):
    return HttpResponse('<h1>Sobre nós</h1>')

def _contato(request):
    return HttpResponse('<h1>Contato</h1>')  

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
