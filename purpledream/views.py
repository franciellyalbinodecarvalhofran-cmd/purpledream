from django.shortcuts import render

def cardapio(request):
    return render(request, "purpledream/cardapio.html")

def login(request):
    return render(request, "purpledream/login.html")

def inicial(request):
    return render(request, "purpledream/index.html")