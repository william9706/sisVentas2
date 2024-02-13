from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articulo/", include("sisVentas.articulo.urls")),
    path("persona/", include("sisVentas.core.urls")),
    path("compra-venta/", include("sisVentas.compra_venta.urls")),
]
