from django.shortcuts import render
from django.views.generic import ListView

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
