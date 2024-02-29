import json

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DeleteView, DetailView, ListView

from sisVentas.compra_venta.forms import (
    IngresoForm,
    detalleIngresosFormSet,
    formset_helper,
)
from sisVentas.compra_venta.models import DetalleDeIngreso, Ingreso


class DetailIngreso(DetailView):
    """
    Vistar para ver un ingreso especifico.
    """

    model = Ingreso
    slug_field: str = "pk"


class IngresoListView(ListView):
    """
    Vista para listar ingresos.
    """

    model = Ingreso
    template_name = "compra_venta/ingreso/ingresos.html"
    context_object_name = "ingresos"
    paginate_by = 15


def crear_ingreso(request):
    """
    Vista basada en funciones para gestionar el proceso de creación de un ingreso.
    """
    ingreso_form = IngresoForm(request.POST or None)
    detalles_ingreso = {}
    if "detalle_ingresos" in request.POST:
        detalle_ingresos = json.loads(request.POST["detalle_ingresos"])
        detalles_ingreso["form-TOTAL_FORMS"] = len(detalle_ingresos)
        detalles_ingreso["form-INITIAL_FORMS"] = 0
        i = 0
        for item in detalle_ingresos:
            detalles_ingreso[f"form-{i}-articulos"] = item["Articulos"]
            detalles_ingreso[f"form-{i}-cantidad"] = item["Cantidad"]
            detalles_ingreso[f"form-{i}-precio_compra"] = item["PrecioCompra"]
            detalles_ingreso[f"form-{i}-precio_venta"] = item["PrecioVenta"]
            i += 1

    detalle_ingreso_formset = detalleIngresosFormSet(data=detalles_ingreso)

    if all([ingreso_form.is_valid(), detalle_ingreso_formset.is_valid()]):
        ingreso_fk = ingreso_form.save()
        detalle_ingreso_formset.save(commit=False)

        for form in detalle_ingreso_formset:
            form.instance.ingresos = ingreso_fk

        detalle_ingreso_formset.save()

        return HttpResponseRedirect(reverse("compra_venta:listar_ingresos"))

    context = {
        "ingreso_form": ingreso_form,
        "formset_detalle_ingresos": detalleIngresosFormSet(
            queryset=DetalleDeIngreso.objects.none()
        ),
        "formset_helper": formset_helper(),
    }
    return render(
        request,
        "compra_venta/ingreso/crear_ingreso.html",
        context=context,
    )


class IngresoDeleteView(SuccessMessageMixin, DeleteView):
    """
    Vista para eliminar Ingreso.
    """

    model = Ingreso
    template_name = "compra_venta/ingreso/eliminar_ingreso.html"
    success_url = reverse_lazy("compra_venta:listar_ingresos")
    success_message = _("Se ha eliminado el ingreso correctamente.")
