from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def cardapio(request):
    return HttpResponse("cardapio.html")

def login(request):
    return HttpResponse("login.html")

def inicial(request):
    return render(request, "index.html")