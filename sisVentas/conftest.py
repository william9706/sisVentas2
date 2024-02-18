import pytest

from sisVentas.articulo.models import Articulo, Categoria
from sisVentas.articulo.tests.factories import ArticuloFactory, CategoriaFactory
from sisVentas.core.models import PerfilPersona
from sisVentas.core.tests.factories import PerfilPersonaFactory


@pytest.fixture
def categoria() -> Categoria:
    return CategoriaFactory()


@pytest.fixture
def articulo() -> Articulo:
    return ArticuloFactory()


@pytest.fixture
def perfil_persona() -> PerfilPersona:
    return PerfilPersonaFactory()
