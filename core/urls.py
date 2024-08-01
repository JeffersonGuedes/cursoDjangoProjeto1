
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse('home')

def sobre(request):
    return HttpResponse('sobre')

def contato(request):
    return HttpResponse('contato')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
