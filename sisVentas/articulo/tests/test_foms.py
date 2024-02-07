import pytest

from sisVentas.articulo.forms import ArticuloForm
from sisVentas.articulo.models import Articulo, Categoria

pytestmark = pytest.mark.django_db


def test_articulo_form(articulo: Articulo, categoria: Categoria):
    """
    Test para probar el correcto funcionamiento del
    formulario ArticuloForm.
    """
    form = ArticuloForm(
        {
            "categoria": categoria.id,
            "codigo": "001",
            "nombre": "prueba",
            "stock": 10,
            "descripcion": "Una descripcion de prueba",
            "imagen": articulo.imagen,
        }
    )

    assert isinstance(form, ArticuloForm)
    assert form.is_valid()
