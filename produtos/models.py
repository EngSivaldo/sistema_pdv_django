from django.db import models

# Create your models here.
# produtos/models.py
# produtos/models.py
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome
