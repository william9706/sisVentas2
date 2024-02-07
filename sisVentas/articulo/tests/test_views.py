import pytest
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from sisVentas.articulo.models import Articulo, Categoria

pytestmark = pytest.mark.django_db


def test_list_view_articulo():
    """
    Verifica que la vista ListaArticulos funcione correctamente.
    Se asegura de que la vista pueda listar y mostrar correctamente los artículos.
    """
    client = Client()

    response = client.get(reverse("articulo:listar_articulos"))
    assert response.status_code == 200


def test_articulo_create_view(articulo: Articulo, categoria: Categoria):
    """
    Test para probar que se pueda crear un articulo correctamente.
    """
    client = Client()
    data = {
        "categoria": categoria.id,
        "codigo": "001",
        "nombre": "prueba",
        "stock": 10,
        "descripcion": "Una descripcion de prueba",
        "imagen": articulo.imagen,
    }
    response = client.post(reverse("articulo:crear_articulo"), data=data)
    articulo = Articulo.objects.get(codigo="001")
    message = list(get_messages(response.wsgi_request))
    assert str(message[0]) == "¡Artículo creado con éxito!"
    assert response.status_code == 302
    assert articulo.nombre == "prueba"
    assert articulo.descripcion == "Una descripcion de prueba"
