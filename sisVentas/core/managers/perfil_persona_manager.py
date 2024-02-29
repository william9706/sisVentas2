from django.db import models

from sisVentas.utils.constantes import TipoPerfilPersona


class PerfilPersonaManager(models.Manager):
    """
    Manager para modelo de Datos de PerfilPersona.
    """

    def obtener_proveedores(self):
        """
        Metodo para obtener los proveedores.
        """
        return super().get_queryset().filter(tipo_persona=TipoPerfilPersona.PROVEEDOR)
