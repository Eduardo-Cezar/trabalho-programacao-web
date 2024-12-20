from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from .models import Prato, Pedido

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from django.contrib import messages
from .forms import PratoForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect

from .forms import CadastroForm

from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Acessar os dados limpos (já validados) do formulário
            
            email = form.cleaned_data['emailLogin']
            senha = form.cleaned_data['senhaLogin']
            # Tentar autenticar o usuário com dados validados
            user = authenticate(request, username=email, password=senha)

            if user is not None:
                # Usuário autenticado com sucesso
                auth_login(request, user)
                return redirect('gerenciarPedido')  # Redireciona para a página do cardápio
            else:
                # E-mail ou senha incorretos
                messages.error(request, 'E-mail ou senha incorretos.')
                return redirect('cadastro')  # Redireciona de volta para a página de login
        else:
            # Caso o formulário não seja válido
            messages.error(request, 'Erro ao validar o formulário.')
            return redirect('login')  # Redireciona de volta para a página de login
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def cadastro(request):
    if request.method == "POST":
        # Inicializa o formulário com os dados do POST
        form = CadastroForm(request.POST)
        if form.is_valid():
            # Salva os dados validados no banco
            form.save()
            return redirect('gerenciarPedido')  # Redireciona após salvar
    else:
        form = CadastroForm()
        
    return render(request, 'cadastro.html', {'form': form})



def gerenciarPedido(request):
    template = loader.get_template('gerenciarPedido.html')
    return HttpResponse(template.render())

@csrf_protect
def cadastrar_prato(request):
    if request.method == 'POST':
        print ("É um formulario")
        print (f"Nome do prato: {request.POST['nome']}" )
        umPrato = Prato(nome = request.POST['nome'], preco = request.POST['preco'], ingredientes = request.POST['ingredientes'])
        umPrato.save()

    return gerenciarpratos(request)

def editar_prato(request, id):
    prato = get_object_or_404(Prato, id=id)  # Busca o prato pelo ID ou retorna 404

    if request.method == 'POST':
        prato.nome = request.POST['nome']
        prato.preco = request.POST['preco']
        prato.ingredientes = request.POST['ingredientes']
        prato.save()

    return gerenciarpratos(request)

def deletar_prato(request, id):
    prato = get_object_or_404(Prato, id=id)  # Busca o prato pelo ID ou retorna 404
    prato.delete()  
    return gerenciarpratos(request) 

@csrf_protect
def gerenciarpratos(request):
    pratosList = Prato.objects.all().values()
    #template = loader.get_template('gerenciarpratos.html')
    context = {
        'pratos': pratosList,
    }


    return render(request, 'gerenciarpratos.html', {'pratos': pratosList})



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
