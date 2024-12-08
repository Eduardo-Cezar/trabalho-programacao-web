from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator

class usuarioCliente(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(
        max_length=11,  
        validators=[RegexValidator(regex=r'^\d+$', message="O telefone deve conter apenas números.")]
    )
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])

    

class usuarioAdministrador(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(
        max_length=11, 
        validators=[RegexValidator(regex=r'^\d+$', message="O telefone deve conter apenas números.")]
    )
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.PositiveIntegerField(validators=[MaxValueValidator(99999)]) 

    
    
class Prato(models.Model):
    nome = models.CharField(max_length=64)
    ingredientes = models.CharField(max_length=1024)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('analise', 'Em Análise'),
        ('aceito', 'Aceito'),
        ('fazendo', 'Fazendo'),
        ('caminho', 'A Caminho'),
        ('entregue', 'Entregue'),
    ]

    prato = models.ManyToManyField(Prato, related_name='pedidos')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='analise')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido #{self.id}"