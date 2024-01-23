from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
# Create your models here.


class Categoria(TimeStampedModel):
    """
    categorias' model
    """
    nombre = models.CharField(_("Nombre del articulo"), max_length=25)
    descripcion = models.CharField(_("Descripcion del articulo"), max_length=50)
    condicion = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Categoria")
        verbose_name_plural = _("Categorias")

    def __str__(self):
        return self.nombre
