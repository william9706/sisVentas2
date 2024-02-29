import pytest
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from sisVentas.compra_venta.models import Ingreso

pytestmark = pytest.mark.django_db


def test_detalle_ingreso(ingreso: Ingreso):
    """
    Test para verificar que la vista DetailIngreso
    funcione correctamente.
    """
    client = Client()
    response = client.get(
        reverse("compra_venta:detalle_ingreso", kwargs={"pk": ingreso.pk})
    )
    assert response.status_code == 200


def test_ingreso_list():
    """
    Test para verificar que la vista IngresoListView
    funcione correctamente.
    """
    client = Client()
    response = client.get(reverse("compra_venta:listar_ingresos"))
    assert response.status_code == 200


def test_eliminar_ingreso(ingreso: Ingreso):
    """
    Test para verificar que se puede eleminar un ingreso.
    """
    client = Client()
    response = client.post(
        reverse("compra_venta:eliminar_ingreso", kwargs={"pk": ingreso.pk})
    )
    message = list(get_messages(response.wsgi_request))
    assert not Ingreso.objects.filter(id=ingreso.pk).exists()
    assert response.status_code == 302
    assert response.url == reverse("compra_venta:listar_ingresos")
    assert str(message[0]) == "Se ha eliminado el ingreso correctamente."


def test_crear_ingreso(ingreso: Ingreso):
    pass
