import pytest

from sisVentas.core.forms import PerfilPersonaForm
from sisVentas.core.models import PerfilPersona
from sisVentas.utils.constantes import TipoDocumento, TipoPerfilPersona

pytestmark = pytest.mark.django_db


def test_perfil_persona_form(perfil_persona: PerfilPersona):
    """
    Test para probar el correcto funcionamiento del
    formulario PerfilPersona.
    """
    form = PerfilPersonaForm(
        {
            "tipo_persona": TipoPerfilPersona.CLIENTE,
            "nombre_persona": "Prueba de un nombre",
            "tipo_documento": TipoDocumento.CC,
            "numero_docuento": "1059044756",
            "direccion": "una direccion",
            "telefono": "3112334354",
            "email": "prueba45@gmail.com",
        }
    )

    assert isinstance(form, PerfilPersonaForm)
    assert form.is_valid()
