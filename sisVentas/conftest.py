import pytest

from sisVentas.articulo.models import Categoria
from sisVentas.articulo.tests.factories import CategoriaFactory


@pytest.fixture
def categoria() -> Categoria:
    return CategoriaFactory()
