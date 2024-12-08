from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('cadastrar_prato/', views.cadastrar_prato, name='cadastrar_prato'),
    path('editar_prato/<int:id>/', views.editar_prato, name='editar_prato'),
    path('deletar_prato/<int:id>/', views.deletar_prato, name='deletar_prato'),
    path('gerenciarPedido/', views.gerenciarPedido, name='gerenciarPedido'),
    path('gerenciarpratos/', views.gerenciarpratos, name='gerenciarpratos'),
    path('finalizarCompra/', views.finalizarCompra, name='finalizarCompra'),
    path('visualizarPedido/', views.visualizarPedido, name='visualizarPedido'),
]

