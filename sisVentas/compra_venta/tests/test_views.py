import json

import pytest
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from sisVentas.compra_venta.models import (
    DetalleDeIngreso,
    DetalleDeVenta,
    Ingreso,
    Venta,
)
from sisVentas.utils.constantes import TipoComprobante

pytestmark = pytest.mark.django_db
User = get_user_model()


def test_detalle_ingreso(ingreso: Ingreso, user: User):  # type: ignore
    """
    Test para verificar que la vista DetailIngreso
    funcione correctamente.
    """
    client = Client()
    client.force_login(user)
    response = client.get(
        reverse("compra_venta:detalle_ingreso", kwargs={"pk": ingreso.pk})
    )
    assert response.status_code == 200


def test_ingreso_list(user: User):  # type: ignore
    """
    Test para verificar que la vista IngresoListView
    funcione correctamente.
    """
    client = Client()
    client.force_login(user)
    response = client.get(reverse("compra_venta:listar_ingresos"))
    assert response.status_code == 200


def test_eliminar_ingreso(ingreso: Ingreso, user: User):  # type: ignore
    """
    Test para verificar que se puede eleminar un ingreso.
    """
    client = Client()
    client.force_login(user)
    response = client.post(
        reverse("compra_venta:eliminar_ingreso", kwargs={"pk": ingreso.pk})
    )
    message = list(get_messages(response.wsgi_request))
    assert not Ingreso.objects.filter(id=ingreso.pk).exists()
    assert response.status_code == 302
    assert response.url == reverse("compra_venta:listar_ingresos")
    assert str(message[0]) == "Se ha eliminado el ingreso correctamente."


def test_crear_ingreso(ingreso: Ingreso, detalle_ingreso: DetalleDeIngreso, user: User):  # type: ignore
    """
    Test para verificar el correcto funcionamiento
    de la vista crear_ingreso.
    """
    client = Client()
    client.force_login(user)
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


def test_venta_list(user: User):  # type: ignore
    """
    Test para probar que la vista VentaListView.
    """
    client = Client()
    client.force_login(user)
    response = client.get(reverse("compra_venta:listar_ventas"))
    assert response.status_code == 200


def test_detalle_venta(venta: Venta, user: User):  # type: ignore
    """
    Prueba para verificar que la vista DetailVenta funcione correctamente.
    """
    client = Client()
    client.force_login(user)
    response = client.get(
        reverse("compra_venta:detalle_venta", kwargs={"pk": venta.pk})
    )
    assert response.status_code == 200


def test_eliminar_venta(venta: Venta, user: User):  # type: ignore
    """
    Prueba para eliminar una venta.
    """
    client = Client()
    client.force_login(user)
    response = client.post(
        reverse("compra_venta:eliminar_venta", kwargs={"pk": venta.pk})
    )
    message = list(get_messages(response.wsgi_request))
    assert response.status_code == 302
    assert str(message[0]) == "Se ha eliminado la venta correctamente."
    assert not Venta.objects.filter(id=venta.pk).exists()
    assert response.url == reverse("compra_venta:listar_ventas")


def test_crear_venta(venta: Venta, detalle_venta: DetalleDeVenta, user: User):  # type: ignore
    """
    Test para verificar el correcto funcionamiento
    de la vista crear_venta.
    """
    client = Client()
    client.force_login(user)
    data = {
        "perfil_persona": venta.perfil_persona.id,
        "tipo_comprobante": TipoComprobante.BOLETA,
        "serie_comprobante": "1235233",
        "numero_comprobante": "1232335",
        "form-TOTAL_FORMS": 2,
        "form-INITIAL_FORMS": 0,
        "detalle_ventas": json.dumps(
            [
                {
                    "Articulos": detalle_venta.articulos.id,
                    "Cantidad": 2,
                    "PrecioVenta": detalle_venta.precio_venta,
                    "Descuento": detalle_venta.descuento,
                },
                {
                    "Articulos": detalle_venta.articulos.id,
                    "Cantidad": 3,
                    "PrecioVenta": detalle_venta.precio_venta,
                    "Descuento": detalle_venta.descuento,
                },
            ]
        ),
    }
    response = client.post(reverse("compra_venta:crear_ventas"), data=data)
    venta = Venta.objects.get(serie_comprobante="1235233")
    message = list(get_messages(response.wsgi_request))
    assert response.status_code == 302
    assert str(message[0]) == "La venta se ha creado correctamente."
    assert venta.tipo_comprobante == TipoComprobante.BOLETA
    assert venta.numero_comprobante == "1232335"
    assert venta.detalledeventa_set.all().exists()
