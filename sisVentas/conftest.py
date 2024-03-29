import pytest

from sisVentas.articulo.models import Articulo, Categoria
from sisVentas.articulo.tests.factories import ArticuloFactory, CategoriaFactory
from sisVentas.compra_venta.models import (
    DetalleDeIngreso,
    DetalleDeVenta,
    Ingreso,
    Venta,
)
from sisVentas.compra_venta.tests.factories import (
    DetalleDeIngresoFactory,
    DetalleDeVentaFactory,
    IngresoFactory,
    VentaFactory,
)
from sisVentas.core.models import PerfilPersona
from sisVentas.core.tests.factories import PerfilPersonaFactory, UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def categoria() -> Categoria:
    return CategoriaFactory()


@pytest.fixture
def articulo() -> Articulo:
    return ArticuloFactory()


@pytest.fixture
def perfil_persona() -> PerfilPersona:
    return PerfilPersonaFactory()


@pytest.fixture
def ingreso() -> Ingreso:
    return IngresoFactory()


@pytest.fixture
def detalle_ingreso() -> DetalleDeIngreso:
    return DetalleDeIngresoFactory()


@pytest.fixture
def venta() -> Venta:
    return VentaFactory()


@pytest.fixture
def detalle_venta() -> DetalleDeVenta:
    return DetalleDeVentaFactory()


@pytest.fixture
def user():
    return UserFactory()
