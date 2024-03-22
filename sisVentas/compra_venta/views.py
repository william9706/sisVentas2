import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DeleteView, DetailView, ListView

from sisVentas.compra_venta.forms import (
    IngresoForm,
    VentaForm,
    detalleIngresosFormSet,
    detalleVentasFormSet,
    formset_helper,
    formset_helper_venta,
)
from sisVentas.compra_venta.models import (
    DetalleDeIngreso,
    DetalleDeVenta,
    Ingreso,
    Venta,
)


class DetailIngreso(LoginRequiredMixin, DetailView):
    """
    Vistar para ver un ingreso especifico.
    """

    model = Ingreso
    slug_field: str = "pk"


class IngresoListView(LoginRequiredMixin, ListView):
    """
    Vista para listar ingresos.
    """

    model = Ingreso
    template_name = "compra_venta/ingreso/ingresos.html"
    context_object_name = "ingresos"
    paginate_by = 15


@login_required
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
        messages.info(request, message=_("El ingreso se ha creado correctamente."))
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


class IngresoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Vista para eliminar Ingreso.
    """

    model = Ingreso
    template_name = "compra_venta/ingreso/eliminar_ingreso.html"
    success_url = reverse_lazy("compra_venta:listar_ingresos")
    success_message = _("Se ha eliminado el ingreso correctamente.")


class VentaListView(LoginRequiredMixin, ListView):
    """
    Vista para listar Ventas.
    """

    model = Venta
    template_name = "compra_venta/venta/ventas.html"
    context_object_name = "ventas"
    paginate_by = 15


class DetailVenta(LoginRequiredMixin, DetailView):
    """
    Vistar para ver una venta especifica.
    """

    model = Venta
    slug_field: str = "pk"


class VentaDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Vista para eliminar Venta.
    """

    model = Venta
    template_name = "compra_venta/venta/eliminar_venta.html"
    success_url = reverse_lazy("compra_venta:listar_ventas")
    success_message = _("Se ha eliminado la venta correctamente.")


@login_required
def crear_venta(request):
    """
    Vista basada en funciones para gestionar el proceso de creación de un ingreso.
    """
    venta_form = VentaForm(request.POST or None)
    detalle_venta = {}
    if "detalle_ventas" in request.POST:
        detalle_ventas = json.loads(request.POST["detalle_ventas"])
        detalle_venta["form-TOTAL_FORMS"] = len(detalle_ventas)
        detalle_venta["form-INITIAL_FORMS"] = 0
        i = 0
        for item in detalle_ventas:
            detalle_venta[f"form-{i}-articulos"] = item["Articulos"]
            detalle_venta[f"form-{i}-cantidad"] = item["Cantidad"]
            detalle_venta[f"form-{i}-precio_venta"] = item["PrecioVenta"]
            detalle_venta[f"form-{i}-descuento"] = item["Descuento"]
            i += 1

    detalle_venta_formset = detalleVentasFormSet(data=detalle_venta)

    if all([venta_form.is_valid(), detalle_venta_formset.is_valid()]):
        venta_fk = venta_form.save()
        detalle_venta_formset.save(commit=False)

        for form in detalle_venta_formset:
            form.instance.ventas = venta_fk

        detalle_venta_formset.save()
        messages.info(request, message=_("La venta se ha creado correctamente."))
        return HttpResponseRedirect(reverse("compra_venta:listar_ventas"))

    context = {
        "venta_form": venta_form,
        "formset_detalle_ventas": detalleVentasFormSet(
            queryset=DetalleDeVenta.objects.none()
        ),
        "formset_helper_venta": formset_helper_venta(),
    }
    return render(
        request,
        "compra_venta/venta/crear_venta.html",
        context=context,
    )
