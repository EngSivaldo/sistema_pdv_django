from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_fornecedores, name='listar_fornecedores'),
    path('novo/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('editar/<int:fornecedor_id>/', views.editar_fornecedor, name='editar_fornecedor'),
    path('excluir/<int:fornecedor_id>/', views.excluir_fornecedor, name='excluir_fornecedor'),
]
