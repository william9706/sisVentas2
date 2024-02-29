import json

import pytest
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from sisVentas.compra_venta.models import DetalleDeIngreso, Ingreso
from sisVentas.utils.constantes import TipoComprobante

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


def test_crear_ingreso(ingreso: Ingreso, detalle_ingreso: DetalleDeIngreso):
    """
    Test para verificar el correcto funcionamiento
    de la vista crear_ingreso.
    """
    client = Client()
    data = {
        "perfil_persona": ingreso.perfil_persona.id,
        "tipo_comprobante": TipoComprobante.BOLETA,
        "serie_comprobante": "1235233",
        "numero_comprobante": "1232335",
        "form-TOTAL_FORMS": 2,
        "form-INITIAL_FORMS": 0,
        "detalle_ingresos": json.dumps(
            [
                {
                    "Articulos": detalle_ingreso.articulos.id,
                    "Cantidad": 2,
                    "PrecioCompra": detalle_ingreso.precio_compra,
                    "PrecioVenta": detalle_ingreso.precio_venta,
                },
                {
                    "Articulos": detalle_ingreso.articulos.id,
                    "Cantidad": 3,
                    "PrecioCompra": detalle_ingreso.precio_compra,
                    "PrecioVenta": detalle_ingreso.precio_venta,
                },
            ]
        ),
    }
    response = client.post(reverse("compra_venta:crear_ingresos"), data=data)
    ingreso = Ingreso.objects.get(serie_comprobante="1235233")
    message = list(get_messages(response.wsgi_request))
    assert response.status_code == 302
    assert str(message[0]) == "El ingreso se ha creado correctamente."
    assert ingreso.tipo_comprobante == TipoComprobante.BOLETA
    assert ingreso.numero_comprobante == "1232335"
    assert ingreso.detalledeingreso_set.all().exists()
