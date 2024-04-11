import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db

User = get_user_model()


def test_articulo_get_method(user: User):  # type: ignore
    """
    Test para probar que el endpoint ArticulosViewSet
    puede listar articulos
    """
    client = Client()
    client.force_login(user)
    response = client.get(reverse("api_articulo:articulo-list"))

    assert response.status_code == status.HTTP_200_OK
