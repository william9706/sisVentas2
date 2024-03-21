from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="account_login", permanent=False)),
    path("admin/", admin.site.urls),
    path("articulo/", include("sisVentas.articulo.urls")),
    path("core/", include("sisVentas.core.urls")),
    path("compra-venta/", include("sisVentas.compra_venta.urls")),
    path("accounts/", include("allauth.urls")),
]
