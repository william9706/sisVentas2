from django.urls import path

from sisVentas.compra_venta.views import IngresoListView, crear_ingreso

app_name = "compra_venta"
urlpatterns = [
    path("listar-ingresos/", view=IngresoListView.as_view(), name="listar_ingresos"),
    path("crear-ingresos/", view=crear_ingreso, name="crear_ingresos"),
]
