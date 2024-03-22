import pytest
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from sisVentas.articulo.models import Articulo, Categoria

pytestmark = pytest.mark.django_db
User = get_user_model()


def test_list_view_articulo(user: User):  # type: ignore
    """
    Verifica que la vista ListaArticulos funcione correctamente.
    Se asegura de que la vista pueda listar y mostrar correctamente los artículos.
    """
    client = Client()
    client.force_login(user)
    response = client.get(reverse("articulo:listar_articulos"))
    assert response.status_code == 200


def test_articulo_create_view(articulo: Articulo, categoria: Categoria, user: User):  # type: ignore
    """
    Test para probar que se pueda crear un articulo correctamente.
    """
    client = Client()
    client.force_login(user)
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


def test_articulo_update_view(articulo: Articulo, categoria: Categoria, user: User):  # type: ignore
    """
    Test para probar que se pueda actualizar un articulo correctamente.
    """
    client = Client()
    client.force_login(user)
    articulo.codigo = "10234566"
    articulo.descripcion = "Prueba de una descripcion"
    articulo.nombre = "Esto es un articulo"
    articulo.stock = 20
    articulo.save()
    data = {
        "categoria": categoria.id,
        "codigo": "001",
        "nombre": "prueba",
        "stock": 10,
        "descripcion": "Una descripcion de prueba",
        "imagen": articulo.imagen,
    }
    response = client.post(
        reverse("articulo:actualizar_articulo", kwargs={"pk": articulo.pk}), data=data
    )
    articulo = Articulo.objects.get(id=articulo.pk)
    message = list(get_messages(response.wsgi_request))
    assert str(message[0]) == "Se ha actualizado el articulo correctamente."
    assert response.status_code == 302
    assert articulo.nombre == "prueba"
    assert articulo.descripcion == "Una descripcion de prueba"


def test_articulo_delete_view(articulo: Articulo, user: User):  # type: ignore
    """
    Test para probar que se pueda eliminar un articulo correctamente.
    """
    client = Client()
    client.force_login(user)
    response = client.post(
        reverse("articulo:eliminar_articulo", kwargs={"pk": articulo.pk})
    )
    message = list(get_messages(response.wsgi_request))
    assert not Articulo.objects.filter(id=articulo.pk).exists()
    assert response.status_code == 302
    assert response.url == reverse("articulo:listar_articulos")
    assert str(message[0]) == "Se ha eliminado el articulo correctamente."
