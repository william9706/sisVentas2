from django.contrib import admin

from sisVentas.articulo.models import Articulo, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    Admin for model Admin.
    """


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    """
    Admin for model Admin.
    """

    list_display = ("nombre", "codigo", "stock")
