from django.urls import path

from sisVentas.compra_venta.views import (
    DetailIngreso,
    DetailVenta,
    IngresoDeleteView,
    IngresoListView,
    VentaDeleteView,
    VentaListView,
    crear_ingreso,
)

app_name = "compra_venta"
urlpatterns = [
    path("listar-ingresos/", view=IngresoListView.as_view(), name="listar_ingresos"),
    path("crear-ingresos/", view=crear_ingreso, name="crear_ingresos"),
    path(
        "eliminar-ingreso/<str:pk>/",
        view=IngresoDeleteView.as_view(),
        name="eliminar_ingreso",
    ),
    path("ingreso/<str:pk>/", view=DetailIngreso.as_view(), name="detalle_ingreso"),
    path("venta/<str:pk>/", view=DetailVenta.as_view(), name="detalle_venta"),
    path("listar-ventas/", view=VentaListView.as_view(), name="listar_ventas"),
    path(
        "eliminar-venta/<str:pk>/",
        view=VentaDeleteView.as_view(),
        name="eliminar_venta",
    ),
]
