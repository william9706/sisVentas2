from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from sisVentas.articulo.forms import ArticuloForm
from sisVentas.articulo.models import Articulo

# Create your views here.


def vista_index(request):
    return render(request, "main.html")


class ListaArticulos(ListView):
    """
    Vista para listar articulos.
    """

    model = Articulo
    template_name = "articulo/listar_articulos.html"
    context_object_name = "listar_articulos"
    paginate_by = 15


class ArticuloCreateView(SuccessMessageMixin, CreateView):
    """
    Vista para crear articulo.
    """

    form_class = ArticuloForm
    model = Articulo
    template_name = "articulo/crear_articulo.html"
    success_message = _("¡Artículo creado con éxito!")
    success_url = reverse_lazy("articulo:listar_articulos")


class ArticuloDeleteView(SuccessMessageMixin, DeleteView):
    """
    Clase para eliminar un Articulo.
    """

    model = Articulo
    template_name = "articulo/delete.html"
    success_url = reverse_lazy("articulo:listar_articulos")
    success_message = _("Se ha eliminado el articulo correctamente.")


class ArticuloUpdateView(SuccessMessageMixin, UpdateView):
    """
    Vista para actualizar articulo.
    """

    form_class = ArticuloForm
    model = Articulo
    success_url = reverse_lazy("articulo:listar_articulos")
    template_name = "articulo/crear_articulo.html"
    success_message = _("Se ha actualizado el articulo correctamente.")
