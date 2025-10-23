from django.db import models

# Create your models here.
# fornecedores/models.py
from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.TextField(blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class EntradaEstoque(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_entrada = models.DateTimeField(auto_now_add=True)
    preco_compra = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} unidades"
