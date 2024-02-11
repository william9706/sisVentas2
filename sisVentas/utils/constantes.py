from collections.abc import Sequence
from typing import Tuple

from django.db import models
from django.utils.translation import gettext_lazy as _


class TipoPerfilPersona(models.IntegerChoices):
    PROVEEDOR: Tuple[int, Sequence[str]] = 1, _("Proveedor")
    CLIENTE: Tuple[int, Sequence[str]] = 2, _("Cliente")


class TipoDocumento(models.IntegerChoices):
    CC: Tuple[int, Sequence[str]] = 1, _("Cédula de ciudadanía")
    TI: Tuple[int, Sequence[str]] = 2, _("Tarjeta de idetidad")
    CE: Tuple[int, Sequence[str]] = 3, _("Cédula extranjería")
