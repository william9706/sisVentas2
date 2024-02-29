from factory import Faker
from factory.django import DjangoModelFactory

from sisVentas.core.models import PerfilPersona
from sisVentas.utils.constantes import TipoDocumento, TipoPerfilPersona


class PerfilPersonaFactory(DjangoModelFactory):
    """
    Factory para modelo Perfilpersona.
    """

    tipo_persona = Faker(
        "random_element", elements=[x[0] for x in TipoPerfilPersona.choices]
    )
    nombre_persona = Faker("name_nonbinary")
    tipo_documento = Faker(
        "random_element", elements=[x[0] for x in TipoDocumento.choices]
    )
    numero_docuento = (
        "1048599685"  # TODO: buscar solucion para Faker correcto con 50 caracteres
    )
    direccion = Faker("address")
    telefono = Faker("msisdn")
    email = Faker("email")

    class Meta:
        model = PerfilPersona
