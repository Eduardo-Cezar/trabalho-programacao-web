from django.db import models

class Prato(models.Model):
    nome = models.CharField(max_length=64)
    ingredientes = models.CharField(max_length=1024)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

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