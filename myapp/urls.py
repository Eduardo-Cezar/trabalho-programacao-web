from django.urls import path
from . import views

urlpatterns = [
    path('gerenciarpratos/', views.gerenciarpratos, name='gerenciarpratos'),
]