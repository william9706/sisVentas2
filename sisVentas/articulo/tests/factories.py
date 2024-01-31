from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from sisVentas.articulo.models import Articulo, Categoria


class CategoriaFactory(DjangoModelFactory):
    """
    Factory para modelo de Datos categoria.
    """

    nombre = Faker("name_nonbinary")
    descripcion = Faker("paragraph", nb_sentences=1)
    condicion = Faker("boolean")

    class Meta:
        model = Categoria


class ArticuloFactory(DjangoModelFactory):
    """
    Factory para modelo de datos Articulo.
    """

    categoria = SubFactory(CategoriaFactory)

    class Meta:
        model = Articulo
