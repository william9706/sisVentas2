import pytest

pytestmark = pytest.mark.django_db

from sisVentas.compra_venta.forms import IngresoForm, VentaForm  # noqa
from sisVentas.compra_venta.models import Ingreso, Venta  # noqa
from sisVentas.utils.constantes import TipoComprobante  # noqa


@pytest.mark.skip(reason="Falta verificar por qué a veces falla.")
def test_ingreso_form(ingreso: Ingreso):
    """
    Test para verificar que el formulario IngresoForm funcione bien.
    """

    form = IngresoForm(
        {
            "perfil_persona": ingreso.perfil_persona,
            "tipo_comprobante": TipoComprobante.BOLETA,
            "serie_comprobante": "1235233",
            "numero_comprobante": "1232335",
        }
    )

    assert isinstance(form, IngresoForm)
    assert form.is_valid()


@pytest.mark.skip(reason="Falta verificar por qué a veces falla.")
def test_venta_form(venta: Venta):
    """
    Test para verificar que el formulario VentaForm funcione bien.
    """

    form = VentaForm(
        {
            "perfil_persona": venta.perfil_persona,
            "tipo_comprobante": TipoComprobante.BOLETA,
            "serie_comprobante": "1235233",
            "numero_comprobante": "1232335",
        }
    )

    assert isinstance(form, IngresoForm)
    assert form.is_valid()
