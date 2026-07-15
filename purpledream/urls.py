from django.urls import path
from . import views

app_name = "purpledream"

urlpatterns = [
    path("cardapio/", views.cardapio, name="cardapio"),
    path("login/", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("carrinho/", views.carrinho, name="carrinho"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("adicionar-carrinho/", views.adicionar_carrinho, name="adicionar_carrinho"),
]
