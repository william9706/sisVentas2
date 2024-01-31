from django.urls import path

from sisVentas.articulo.views import ListaArticulos, vista_index

app_name = "articulo"
urlpatterns = [
    path("", view=vista_index, name="index"),
    path("index/", view=ListaArticulos.as_view(), name="listar_articulos"),
]
