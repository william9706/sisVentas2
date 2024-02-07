import pytest

from sisVentas.articulo.models import Articulo, Categoria
from sisVentas.articulo.tests.factories import (ArticuloFactory,
                                                CategoriaFactory)


@pytest.fixture
def categoria() -> Categoria:
    return CategoriaFactory()


@pytest.fixture
def articulo() -> Articulo:
    return ArticuloFactory()
