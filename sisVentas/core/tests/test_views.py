import pytest
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from sisVentas.core.models import PerfilPersona
from sisVentas.utils.constantes import TipoDocumento, TipoPerfilPersona

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


def test_perfil_persona_update_view(perfil_persona: PerfilPersona):
    """
    Test para probar que la vista PerfilPersonaUpdateview
    funcione correctamente y se pueda actualizar un registro.
    """
    cliet = Client()
    perfil_persona.tipo_documento = TipoDocumento.CE
    perfil_persona.nombre_persona = "Jose alberto"
    perfil_persona.numero_docuento = "1846755843"
    perfil_persona.save()
    data = {
        "tipo_persona": TipoPerfilPersona.CLIENTE,
        "tipo_documento": TipoDocumento.CC,
        "nombre_persona": "Prueba de un nombre",
        "numero_docuento": "1059044756",
    }
    response = cliet.post(
        reverse("persona:actualizar_persona", kwargs={"pk": perfil_persona.pk}),
        data=data,
    )
    perfil_persona = PerfilPersona.objects.get(id=perfil_persona.pk)
    message = list(get_messages(response.wsgi_request))
    assert str(message[0]) == "Persona actualizada correctamente."
    assert response.status_code == 302
    assert perfil_persona.tipo_persona == TipoPerfilPersona.CLIENTE
    assert perfil_persona.nombre_persona == "Prueba de un nombre"
    assert perfil_persona.numero_docuento == "1059044756"


def test_perfil_persona_delete_view(perfil_persona: PerfilPersona):
    """
    Test para probar que la vista PerfilPersonaDeleteview
    funcione correctamente.
    """
    client = Client()
    response = client.post(
        reverse("persona:eliminar_persona", kwargs={"pk": perfil_persona.pk})
    )
    message = list(get_messages(response.wsgi_request))
    assert not PerfilPersona.objects.filter(id=perfil_persona.pk).exists()
    assert response.status_code == 302
    assert str(message[0]) == "Persona eliminada correctamente."
    assert response.url == reverse("persona:listar_personas")
