from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from sisVentas.articulo.tests.factories import ArticuloFactory
from sisVentas.compra_venta.models import DetalleDeIngreso, Ingreso
from sisVentas.core.tests.factories import PerfilPersonaFactory
from sisVentas.utils.constantes import TipoComprobante


class IngresoFactory(DjangoModelFactory):
    """
    Factory para modelo de Datos Ingreso.
    """

    perfil_persona = SubFactory(PerfilPersonaFactory)
    tipo_comprobante = Faker(
        "random_element", elements=[x[0] for x in TipoComprobante.choices]
    )
    serie_comprobante = (
        "2345434"  # TODO: buscar solucion para Faker correcto hasta 50 caracteres
    )
    numero_comprobante = (
        "434555"  # TODO: buscar solucion para Faker correcto hasta 50 caracteres
    )
    impuesto = 0

    estado = Faker(
        "random_element", elements=[x[0] for x in Ingreso.EstadoImpuesto.choices]
    )

    class Meta:
        model = Ingreso


class DetalleDeIngresoFactory(DjangoModelFactory):
    """
    Factory para modelo de Datos DetalleDeIngreso.
    """

    articulos = SubFactory(ArticuloFactory)
    ingresos = SubFactory(IngresoFactory)
    cantidad = 4
    precio_compra = 4000
    precio_venta = 5000

    class Meta:
        model = DetalleDeIngreso
