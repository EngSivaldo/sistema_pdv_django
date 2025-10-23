from django.shortcuts import render, redirect
from .models import Venda, ItemVenda
from clientes.models import Cliente
from produtos.models import Produto
from django.contrib import messages
from fornecedores.models import Fornecedor
from vendas.models import Venda


from decimal import Decimal



def home(request):
    total_produtos = Produto.objects.count()
    total_clientes = Cliente.objects.count()
    total_fornecedores = Fornecedor.objects.count()
    total_vendas = Venda.objects.count()

    context = {
        'total_produtos': total_produtos,
        'total_clientes': total_clientes,
        'total_fornecedores': total_fornecedores,
        'total_vendas': total_vendas,
    }
    return render(request, 'vendas/home.html', context)

def fazer_venda(request):
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    resumo = None  # para exibir o resumo da venda após salvar

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        cliente = Cliente.objects.get(id=cliente_id)

        produtos_ids = request.POST.getlist('produto')
        quantidades = request.POST.getlist('quantidade')

        venda = Venda.objects.create(cliente=cliente, total=0)
        total_geral = Decimal('0.00')
        itens_resumo = []

        for prod_id, qtd in zip(produtos_ids, quantidades):
            if not prod_id:
                continue
            produto = Produto.objects.get(id=prod_id)
            qtd = int(qtd)
            subtotal = produto.preco * qtd
            ItemVenda.objects.create(venda=venda, produto=produto, quantidade=qtd, subtotal=subtotal)
            total_geral += subtotal
            itens_resumo.append((produto.nome, qtd, subtotal))

            # Atualiza estoque
            produto.estoque -= qtd
            produto.save()

        venda.total = total_geral
        venda.save()

        resumo = {
            'cliente': cliente.nome,
            'itens': itens_resumo,
            'total': total_geral
        }

        messages.success(request, f'✅ Venda realizada com sucesso para {cliente.nome}! Total: R$ {total_geral:.2f}')

    return render(request, 'vendas/fazer_venda.html', {
        'clientes': clientes,
        'produtos': produtos,
        'resumo': resumo
    })



def listar_vendas(request):
    vendas = Venda.objects.all().order_by('-id')  # últimas vendas primeiro
    return render(request, 'vendas/listar.html', {'vendas': vendas})