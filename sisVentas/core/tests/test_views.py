import pytest
from django.test import Client
from django.urls import reverse

from sisVentas.core.models import PerfilPersona

pytestmark = pytest.mark.django_db


def test_perfil_persona_list_view():
    """
    Test para probar el correcto funcionamiento de la vista PerfilPersonaListView.
    """
    client = Client()

    response = client.get(reverse("persona:listar_personas"))
    assert response.status_code == 200


def test_perfil_persona_create_view(perfil_persona: PerfilPersona):
    """
    Test para probar que la clase PerfilPersonaCreateView funcione
    correctamente y pertmita crear un perfil de la persona.
    """
    client = Client()
    data = {
        "tipo_persona": perfil_persona.tipo_persona,
        "nombre_persona": "Nombre de prueba",
        "tipo_documento": perfil_persona.tipo_documento,
        "numero_docuento": "1956877643",
        "direccion": "una direccion",
        "telefono": "3225446576",
        "email": "PruebaEmail@gmail.com",
    }
    response = client.post(reverse("persona:crear_persona"), data=data)
    registro = PerfilPersona.objects.get(numero_docuento="1956877643")
    assert response.status_code == 302
    assert registro.nombre_persona == "Nombre de prueba"
    assert registro.numero_docuento == "1956877643"
