from django.urls import include, path

urlpatterns = [
    path("articulos/", include("sisVentas.articulo.api.api_urls")),
]
