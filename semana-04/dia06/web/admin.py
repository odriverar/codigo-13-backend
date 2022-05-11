from django.contrib import admin

# Register your models here.
from .models import Categoria, Cliente, Pedido, PedidoDetalle, Producto

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(PedidoDetalle)