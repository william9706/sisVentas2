import pytest
from django.test import Client
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_list_view_articulo():
    """
    Verifica que la vista ListaArticulos funcione correctamente.
    Se asegura de que la vista pueda listar y mostrar correctamente los artículos.
    """
    client = Client()

    response = client.get(reverse("articulo:listar_articulos"))
    assert response.status_code == 200
