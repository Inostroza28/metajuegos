from django.contrib import admin
from .models import Credencial, Producto, Carrito

# Register your models here.
admin.site.register(Credencial)
admin.site.register(Producto)
admin.site.register(Carrito)
