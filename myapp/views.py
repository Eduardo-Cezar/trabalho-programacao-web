from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from .models import Prato, Pedido
from .forms import CadastroForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Recuperar os dados do formulário
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            # Tentar autenticar o usuário
            user = authenticate(request, username=email, password=senha)

            if user is not None:
                # Usuário autenticado com sucesso
                auth_login(request, user)
                return redirect('home')  # Redireciona para a página inicial após login, tem que mudar para a pagina do cardapio que ainda não existe
            else:
                # E-mail ou senha incorretos
                messages.error(request, 'E-mail ou senha incorretos.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            # Salvar os dados no banco
            form.save()

            
            return redirect('gerenciarPedido')   
    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form})

def gerenciarPedido(request):
    template = loader.get_template('gerenciarPedido.html')
    return HttpResponse(template.render())

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
