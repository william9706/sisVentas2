import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_articulo_get_method():
    """
    Test para probar que el endpoint ArticulosViewSet
    puede listar articulos
    """
    client = Client()
    response = client.get(reverse("api_articulo:articulo-list"))

    assert response.status_code == status.HTTP_200_OK
