from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venda #{self.id} - {self.cliente.nome if self.cliente else 'Cliente'}"

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    quantidade = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Calcula subtotal automaticamente
        if self.produto:
            self.subtotal = self.quantidade * self.produto.preco
        super().save(*args, **kwargs)
