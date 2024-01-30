from django.urls import path, include
from sisVentas.articulo.views import vista_index, ListaArticulos

urlpatterns = [
    path("", view=vista_index, name="index"),
    path("index/", view=ListaArticulos.as_view(), name="listar_articulos")
]
