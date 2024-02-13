from django.contrib import admin

from sisVentas.core.models import PerfilPersona


@admin.register(PerfilPersona)
class PerfilPersonaAdmin(admin.ModelAdmin):
    """
    Admiinistrador para el modelo PerfilPersona.
    """

    list_display = (
        "tipo_persona",
        "nombre_persona",
        "tipo_documento",
        "telefono",
        "email",
    )
