from django.contrib import admin

from sisVentas.compra_venta.models import Ingreso, Venta


@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    """
    Administrador para modelo Ingreso.
    """


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    """
    Administrador para modelo Venta.
    """
