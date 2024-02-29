from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from sisVentas.core.managers.perfil_persona_manager import PerfilPersonaManager
from sisVentas.utils.constantes import TipoDocumento, TipoPerfilPersona


class PerfilPersona(TimeStampedModel):
    """
    Modelo creado para gestionar todos los perfiles
    relacionados con el usurio.
    """

    tipo_persona = models.PositiveSmallIntegerField(
        _("Tiopo de persona"),
        choices=TipoPerfilPersona.choices,
        default=TipoPerfilPersona.CLIENTE,
    )
    nombre_persona = models.CharField(
        _("Nombre de la persona"), max_length=100, null=False, blank=False
    )
    tipo_documento = models.PositiveSmallIntegerField(
        _("Tipo de documento"),
        choices=TipoDocumento.choices,
        default=TipoDocumento.CC,
        null=False,
        blank=False,
    )
    numero_docuento = models.CharField(
        _("Numero de documento"),
        max_length=15,
        null=False,
        blank=False,
    )
    direccion = models.CharField(
        _("Direccion de residencia"),
        max_length=70,
        null=True,
        blank=True,
    )
    telefono = models.CharField(
        _("Telefono"),
        max_length=15,
        null=True,
        blank=True,
    )
    email = models.CharField(
        _("Correo electronico"),
        max_length=50,
        null=True,
        blank=True,
    )
    perfil = PerfilPersonaManager()

    def __str__(self):
        return self.nombre_persona

    class Meta:
        verbose_name = _("Persona")
        verbose_name_plural = _("Personas")
