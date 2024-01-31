from collections.abc import Sequence
from typing import Tuple

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Categoria(TimeStampedModel):
    """
    categoria's model
    """

    nombre = models.CharField(_("Nombre de la categoria"), max_length=25)
    descripcion = models.CharField(_("Descripcion de la categoria"), max_length=50)
    condicion = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Categoria")
        verbose_name_plural = _("Categorias")

    def __str__(self):
        return self.nombre


class Articulo(TimeStampedModel):
    """
    Article model for managing article data.
    """

    class EstadoFactura(models.IntegerChoices):
        ERROR: Tuple[int, Sequence[str]] = 1, _("Error en la factura")
        PRESENTADA: Tuple[int, Sequence[str]] = 2, _("Factura radicada")
        BORRADOR: Tuple[int, Sequence[str]] = 3, _("Factura sin radicar")

    categoria = models.ForeignKey(
        Categoria,
        verbose_name=_("Categoria"),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    codigo = models.CharField(
        _("Codigo"),
        null=False,
        blank=False,
        max_length=50,
    )
    nombre = models.CharField(
        _("Nombre"),
        null=False,
        blank=False,
        max_length=150,
    )
    stock = models.IntegerField(
        verbose_name=_("Stock"),
        null=False,
        blank=False,
    )
    descripcion = models.TextField(
        _("Descripcion"),
        null=True,
        blank=True,
        max_length=500,
    )
    imagen = models.ImageField(upload_to="media/articulos", blank=True, null=True)
    estado = models.PositiveSmallIntegerField(
        _("Estado del articulo"),
        choices=EstadoFactura.choices,
        default=EstadoFactura.BORRADOR,
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _("Articulo")
        verbose_name_plural = _("Articulos")
