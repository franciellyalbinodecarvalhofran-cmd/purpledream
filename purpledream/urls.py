from django.urls import path
from . import views

app_name = "purpledream"

urlpatterns = [
    path("cardapio/", views.cardapio, name="cardapio"),
    path("login/", views.login, name="login"),
    path("inicial/", views.inicial, name="inicial"),
    
]
