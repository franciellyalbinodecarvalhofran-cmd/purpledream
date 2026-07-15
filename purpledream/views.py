from decimal import Decimal
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


def _get_carrinho(request):
    return request.session.get("carrinho", [])


def _salvar_carrinho(request, carrinho):
    request.session["carrinho"] = carrinho
    request.session.modified = True


def cardapio(request):
    return render(request, "purpledream/cardapio.html")


def login(request):
    return render(request, "purpledream/login.html")


def home(request):
    return render(request, "purpledream/home.html")


def carrinho(request):
    carrinho = _get_carrinho(request)
    itens = []
    subtotal = Decimal("0.00")

    for item in carrinho:
        preco = Decimal(str(item.get("preco", 0)))
        quantidade = int(item.get("quantidade", 1))
        total_item = preco * quantidade
        subtotal += total_item
        itens.append(
            {
                "produto_id": item.get("produto_id"),
                "nome": item.get("nome", "Produto"),
                "preco": preco,
                "quantidade": quantidade,
                "total_item": total_item,
            }
        )

    total = subtotal + Decimal("5.00")
    return render(
        request,
        "purpledream/carrinho.html",
        {
            "itens": itens,
            "quantidade_total": sum(item["quantidade"] for item in itens),
            "subtotal": subtotal,
            "total": total,
        },
    )


def adicionar_carrinho(request):
    if request.method == "POST":
        produto_id = request.POST.get("produto_id")
        nome = request.POST.get("nome", "Produto")
        preco = request.POST.get("preco", "0")

        carrinho = _get_carrinho(request)
        item_encontrado = None
        for item in carrinho:
            if item.get("produto_id") == produto_id:
                item_encontrado = item
                break

        if item_encontrado is None:
            carrinho.append(
                {
                    "produto_id": produto_id,
                    "nome": nome,
                    "preco": preco,
                    "quantidade": 1,
                }
            )
        else:
            item_encontrado["quantidade"] = int(item_encontrado.get("quantidade", 0)) + 1

        _salvar_carrinho(request, carrinho)

    return redirect("purpledream:carrinho")


def catalogo(request):
    return render(request, "purpledream/catalogo.html")