from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm  # supondo que você tenha um form para Cliente

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes_list.html', {'clientes': clientes})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/cliente_form.html', {'form': form})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/cliente_confirm_delete.html', {'cliente': cliente})



def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastrar.html', {'form': form})
