from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import (
    Cliente, Empleado, Orden, DetalleOrden,
    Producto, Proveedor, Categoria
)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id_cliente", "cli_nombre", "cli_contacto", "cli_mail")
    search_fields = ("id_cliente", "cli_nombre", "cli_mail")

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("id_empleado", "emp_nombre", "emp_apellido", "emp_mail")
    search_fields = ("emp_nombre", "emp_apellido")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id_categoria", "cat_nombre")
    search_fields = ("cat_nombre",)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id_producto", "pro_nombre", "pro_precio", "pro_stock")
    search_fields = ("pro_nombre",)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("id_proveedor", "prv_empresa", "prv_giro", "prv_telefono")
    search_fields = ("prv_empresa", "prv_giro")

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ("id_orden", "id_cliente", "id_empleado", "ord_fecha")
    search_fields = ("id_cliente__cli_nombre",)

@admin.register(DetalleOrden)
class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = ("id_detalle", "orden", "producto", "cantidad", "precio_unitario")
    search_fields = ("orden__id_orden", "producto__pro_nombre")
>>>>>>> 279826a (Primer commit: Proyecto Django con modelos y admin)
