from django.contrib import admin

from sisVentas.compra_venta.models import (
    DetalleDeIngreso,
    DetalleDeVenta,
    Ingreso,
    Venta,
)


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


@admin.register(DetalleDeIngreso)
class DetalleDeIngresoAdmin(admin.ModelAdmin):
    """
    Administrador para modelo DetalleDeIngreso
    """


@admin.register(DetalleDeVenta)
class DetalleDeVentaAdmin(admin.ModelAdmin):
    """
    Administrador para modelo DetalleDeVenta
    """
