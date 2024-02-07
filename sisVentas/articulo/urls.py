from django.urls import path

from sisVentas.articulo.views import (ArticuloCreateView, ArticuloDeleteView,
                                      ArticuloUpdateView, ListaArticulos,
                                      vista_index)

app_name = "articulo"
urlpatterns = [
    path("", view=vista_index, name="index"),
    path("index/", view=ListaArticulos.as_view(), name="listar_articulos"),
    path("nuevo-articulo/", view=ArticuloCreateView.as_view(), name="crear_articulo"),
    path(
        "actualizar-articulo/<str:pk>/",
        view=ArticuloUpdateView.as_view(),
        name="actualizar_articulo",
    ),
    path(
        "eliminar-articulo/<str:pk>/",
        view=ArticuloDeleteView.as_view(),
        name="eliminar_articulo",
    ),
]
