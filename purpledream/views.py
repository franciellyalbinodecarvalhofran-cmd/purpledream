

from django.shortcuts import render
from django.http import HttpResponse

def cardapio(request):
    return render("cardapío.html")

def login(request):
    return render("login.html")

def inicial(request):
    return render(request, "index.html")