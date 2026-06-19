from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def cardapio(request):
    return HttpResponse("cardapío")

def login(request):
    return HttpResponse("login")

def inicial(request):
    return render(request, "index.html")