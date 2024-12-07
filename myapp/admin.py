from django.contrib import admin
from .models import Prato, Pedido

admin.site.register(Prato)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'total')  
    list_filter = ('status',)  
    search_fields = ('id',)  
    filter_horizontal = ('prato',)  

