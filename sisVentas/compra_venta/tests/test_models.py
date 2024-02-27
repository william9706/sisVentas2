import pytest

from sisVentas.compra_venta.models import DetalleDeIngreso, Ingreso

pytestmark = pytest.mark.django_db


def test_calcular_total_ingreso(ingreso: Ingreso, detalle_ingreso: DetalleDeIngreso):
    """
    Test para verificar el correcto funcionamiento del método privado _calcular_total_ingreso.
    """
    detalle_ingreso.ingresos = ingreso
    detalle_ingreso.save()
    assert ingreso._calcular_total_ingreso() == 16000


def test_obtener_total_ingresos(ingreso: Ingreso, detalle_ingreso: DetalleDeIngreso):
    """
    Test para verificar el correcto funcionamiento de la propiedad _obtener_total_ingresos.
    """
    detalle_ingreso.ingresos = ingreso
    detalle_ingreso.save()
    assert ingreso.obtener_total_ingresos == 16000
