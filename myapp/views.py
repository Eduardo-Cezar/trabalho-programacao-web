from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from .models import Prato, Pedido

def gerenciarpratos(request):
    template = loader.get_template('gerenciarpratos.html')
    return HttpResponse(template.render())

def finalizarCompra(request):
    if request.method == 'POST':
        return JsonResponse({'mensagem': 'Compra finalizada com sucesso!'})
    
    pratosDisponiveis = Prato.objects.all()
    valorTotal = sum(prato.preco for prato in pratosDisponiveis)

    return render(request, 'finalizarCompra.html', {'pratos': pratosDisponiveis, 'valor_total': valorTotal})

def visualizarPedido(request):
    pedidos = Pedido.objects.prefetch_related('prato').all()

    pedidosContexto = []

    for pedido in pedidos:
        pratosPedido = pedido.prato.all()
        pedidosContexto.append({
            'id': pedido.id,
            'pratos': pratosPedido,
            'status': pedido.status,
            'total': pedido.total
        })

    return render(request, 'visualizarPedido.html', {'pedidos': pedidosContexto})
