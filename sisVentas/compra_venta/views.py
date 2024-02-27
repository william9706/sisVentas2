from django.views.generic import ListView

from sisVentas.compra_venta.models import Ingreso


class IngresoListView(ListView):
    """
    Vista para listar ingresos.
    """

    model = Ingreso
    template_name = "compra_venta/ingreso/ingresos.html"
    context_object_name = "ingresos"
    paginate_by = 15
