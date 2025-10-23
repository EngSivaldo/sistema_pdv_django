from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Fornecedor
from .forms import FornecedorForm

def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/fornecedores_list.html', {'fornecedores': fornecedores})

def cadastrar_fornecedor(request):
    form = FornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Fornecedor cadastrado com sucesso!")
        return redirect('listar_fornecedores')
    
    # aqui estava 'fornecedores/cadastrar.html'
    return render(request, 'fornecedores/cadastrar_fornecedor.html', {'form': form})


def editar_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    form = FornecedorForm(request.POST or None, instance=fornecedor)
    if form.is_valid():
        form.save()
        messages.success(request, "Fornecedor atualizado com sucesso!")
        return redirect('listar_fornecedores')
    return render(request, 'fornecedores/cadastrar.html', {'form': form})

def excluir_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    fornecedor.delete()
    messages.success(request, "Fornecedor excluído com sucesso!")
    return redirect('listar_fornecedores')
