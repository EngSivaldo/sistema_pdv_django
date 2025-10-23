from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fazer-venda/', views.fazer_venda, name='fazer_venda'),
    path('listar/', views.listar_vendas, name='listar_vendas'),  # 👈 adicionar

]
