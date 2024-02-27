from django.urls import path

from sisVentas.compra_venta.views import IngresoListView

app_name = "compra_venta"
urlpatterns = [
    path("listar-ingresos/", view=IngresoListView.as_view(), name="listar_ingresos")
]
