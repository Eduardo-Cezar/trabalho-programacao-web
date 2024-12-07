from django.urls import path
from . import views

urlpatterns = [
    path('gerenciarpratos/', views.gerenciarpratos, name='gerenciarpratos'),
    path('finalizarCompra/', views.finalizarCompra, name='finalizarCompra'),
    path('visualizarPedido/', views.visualizarPedido, name='visualizarPedido'),
]

