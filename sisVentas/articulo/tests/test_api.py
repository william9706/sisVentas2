import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from sisVentas.articulo.models import Articulo

pytestmark = pytest.mark.django_db

User = get_user_model()


def test_articulo_get_method(user: User, articulo: Articulo):  # type: ignore
    """
    Test para probar que el endpoint ArticulosViewSet
    puede listar articulos
    """
    client = APIClient()
    articulo.nombre = "Articulo 1"
    articulo.descripcion = "Descripcion 1"
    articulo.stock = 10
    articulo.save()
    client.force_login(user)
    response = client.get(reverse("api_articulo:articulo-list"))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0]["nombre"] == "Articulo 1"
    assert response.json()[0]["descripcion"] == "Descripcion 1"
    assert response.json()[0]["stock"] == 10


def test_articulo_post_method(user: User, articulo: Articulo):  # type: ignore
    """
    Test para probar el comportamiento del endpoint ArticulosViewSet
    cuando se hace una solicitud post.
    """
    client = APIClient()
    client.force_login(user)
    data = {
        "categoria": articulo.categoria.id,
        "codigo": "123456",
        "nombre": "Nombre Bonito",
        "stock": 10,
        "descripcion": "Una descripcion",
        # "imagen": articulo.imagen,
    }
    # TODO: buscar forma de enviar una imagen usando mock
    response = client.post(
        reverse("api_articulo:articulo-list"), data=data, format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["nombre"] == "Nombre Bonito"
    assert response.json()["descripcion"] == "Una descripcion"
    assert response.json()["stock"] == 10
    assert response.json()["codigo"] == "123456"
