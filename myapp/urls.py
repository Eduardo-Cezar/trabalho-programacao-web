from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('gerenciarPedido/', views.gerenciarPedido, name='gerenciarPedido'),
    path('gerenciarpratos/', views.gerenciarpratos, name='gerenciarpratos'),
    path('finalizarCompra/', views.finalizarCompra, name='finalizarCompra'),
    path('visualizarPedido/', views.visualizarPedido, name='visualizarPedido'),
]

