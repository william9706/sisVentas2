from factory import Faker, SubFactory
from factory.django import DjangoModelFactory, ImageField

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
    codigo = Faker("numerify")
    nombre = Faker("name_nonbinary")
    stock = Faker("numerify", text="####")
    descripcion = Faker("paragraph", nb_sentences=1)
    imagen = ImageField(color="red")
    estado = Faker(
        "random_element", elements=[x[0] for x in Articulo.EstadoArticulo.choices]
    )

    class Meta:
        model = Articulo
