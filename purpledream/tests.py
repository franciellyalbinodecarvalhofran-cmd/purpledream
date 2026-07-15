from django.test import SimpleTestCase
from django.urls import reverse


class CarrinhoTests(SimpleTestCase):
    def test_adicionar_produto_cria_item_no_carrinho(self):
        response = self.client.post(
            reverse("purpledream:adicionar_carrinho"),
            {
                "produto_id": "trufas",
                "nome": "Trufas",
                "preco": "15.00",
            },
        )

        self.assertEqual(response.status_code, 302)
        carrinho = self.client.session.get("carrinho", [])
        self.assertEqual(len(carrinho), 1)
        self.assertEqual(carrinho[0]["produto_id"], "trufas")
        self.assertEqual(carrinho[0]["quantidade"], 1)
