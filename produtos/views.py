from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProdutoForm
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos_list.html', {'produtos': produtos})

def cadastrar_produto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Produto cadastrado com sucesso!")
        return redirect('listar_produtos')  # redireciona para a lista

    return render(request, 'produtos/cadastrar.html', {'form': form})


def editar_produto(request, id):
    # por enquanto só redireciona para a lista
    return redirect('listar_produtos')

def excluir_produto(request, id):
    # por enquanto só redireciona para a lista
    return redirect('listar_produtos')
