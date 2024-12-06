from django.db import models

class pratos(models.Model):
    nome = models.CharField(max_length=64)
    ingredientes = models.CharField(max_length=1024)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
