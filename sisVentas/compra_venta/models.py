from collections.abc import Sequence
from typing import Tuple

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from sisVentas.articulo.models import Articulo
from sisVentas.core.models import PerfilPersona
from sisVentas.utils.constantes import TipoComprobante


class Ingreso(TimeStampedModel):
    """
    Modelado de datos para un ingreso.
    """

    class EstadoImpuesto(models.IntegerChoices):
        ACTIVO: Tuple[int, Sequence[str]] = 2, _("Activo")
        INACTIVO: Tuple[int, Sequence[str]] = 3, _("Inactivo")

    perfil_persona = models.ForeignKey(
        PerfilPersona,
        verbose_name=_("Perfil persona"),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    articulos = models.ManyToManyField(
        Articulo,
        verbose_name=_("Articulos"),
        related_name="ingreso_articulos",
    )

    tipo_comprobante = models.CharField(
        _("Tipo de compronbante"),
        choices=TipoComprobante.choices,
        default=TipoComprobante.BOLETA,
    )
    serie_comprobante = models.CharField(
        _("Serie de compronbante"),
        max_length=7,
        null=False,
        blank=False,
    )
    numero_comprobante = models.CharField(
        _("Nunmero de compronbante"),
        max_length=10,
        null=False,
        blank=False,
    )
    impuesto = models.FloatField(
        _("Impuesto del ingreso"),
        null=False,
        blank=False,
    )
    precio_compra = models.DecimalField(
        _("Precio de compra"),
        null=False,
        blank=False,
        decimal_places=2,
        max_digits=12,
        default=0,
    )
    precio_venta = models.DecimalField(
        _("Precio de venta"),
        null=False,
        blank=False,
        decimal_places=2,
        max_digits=12,
        default=0,
    )
    estado = models.PositiveBigIntegerField(
        _("Estado del ingreso"),
        choices=EstadoImpuesto.choices,
        default=EstadoImpuesto.ACTIVO,
    )

    def __str__(self):
        return self.serie_comprobante

    class Meta:
        verbose_name = _("Ingreso")
        verbose_name_plural = _("Ingresos")


class Venta(TimeStampedModel):
    """
    Modelado de datos para una Venta.
    """

    class EstadoImpuesto(models.IntegerChoices):
        ACTIVO: Tuple[int, Sequence[str]] = 2, _("Activo")
        INACTIVO: Tuple[int, Sequence[str]] = 3, _("Inactivo")

    perfil_persona = models.ForeignKey(
        PerfilPersona,
        verbose_name=_("Perfil persona"),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    articulos = models.ManyToManyField(
        Articulo,
        verbose_name=_("Articulos"),
        related_name="venta_articulos",
    )

    tipo_comprobante = models.CharField(
        _("Tipo de compronbante"),
        choices=TipoComprobante.choices,
        default=TipoComprobante.BOLETA,
    )
    serie_comprobante = models.CharField(
        _("Serie de compronbante"),
        max_length=7,
        null=False,
        blank=False,
    )
    numero_comprobante = models.CharField(
        _("Nunmero de compronbante"),
        max_length=10,
        null=False,
        blank=False,
    )
    impuesto = models.FloatField(
        _("Impuesto de la venta"),
        null=False,
        blank=False,
    )
    precio_venta = models.DecimalField(
        _("Precio de venta"),
        null=False,
        blank=False,
        decimal_places=2,
        max_digits=12,
        default=0,
    )
    descuento = models.DecimalField(
        _("Descuento de la venta"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=12,
        default=0,
    )
    estado = models.PositiveBigIntegerField(
        _("Estado de la venta"),
        choices=EstadoImpuesto.choices,
        default=EstadoImpuesto.ACTIVO,
    )

    def __str__(self):
        return self.serie_comprobante

    class Meta:
        verbose_name = _("Venta")
        verbose_name_plural = _("Ventas")
