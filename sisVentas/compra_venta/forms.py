from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout
from django import forms
from django.forms.models import modelformset_factory
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from sisVentas.compra_venta.models import DetalleDeIngreso, Ingreso
from sisVentas.core.models import PerfilPersona


class IngresoForm(forms.ModelForm):
    """
    Formulario para gerstionar modelo de datos
    Ingreso.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[
            "perfil_persona"
        ].queryset = PerfilPersona.perfil.obtener_proveedores()
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.error_text_inline = True
        self.helper.form_id = "formulario-ingreso"
        self.helper.form_action = reverse_lazy("articulo:crear_articulo")
        self.helper.form_tag = False
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            Fieldset(
                _("Nuevo Ingreso"),
                Field("perfil_persona", css_class="select-form"),
            ),
            Div(
                Field("tipo_comprobante", css_class="select-form"),
                "detalle_ingresos",
                css_class="col-lg-4 col-sm-4 col-md-4 col-xs-12",
            ),
            Div(
                Field(
                    "serie_comprobante",
                    wrapper_class="input-group input-group-static my-4 form_dinamic",
                ),
                css_class="col-lg-4 col-sm-4 col-md-4 col-xs-12",
            ),
            Div(
                Field(
                    "numero_comprobante",
                    wrapper_class="input-group my-4 input-group-static",
                ),
                css_class="col-lg-4 col-sm-4 col-md-4 col-xs-12",
            ),
        )

        self.fields["perfil_persona"].label = "Proveedor"

    detalle_ingresos = forms.JSONField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Ingreso
        exclude = ["articulos", "impuesto", "estado"]


class DetalleDeIngresoForm(forms.ModelForm):
    """
    Formulario para modelo DetalleDeIngreso.
    """

    class Meta:
        model = DetalleDeIngreso
        exclude = ["ingresos"]


detalleIngresosFormSet = modelformset_factory(
    DetalleDeIngreso, form=DetalleDeIngresoForm, extra=1
)


def formset_helper():
    helper = FormHelper()
    helper.form_method = "POST"
    helper.error_text_inline = True
    helper.form_id = "formulario-detalle-ingreso"
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Field("articulos"),
            css_class="col-lg-4 col-sm-4 col-md-4 col-xs-12",
        ),
        Div(
            Field(
                "cantidad",
                wrapper_class="input-group input-group-static my-4",
            ),
            css_class="col-lg-2 col-sm-2 col-md-2 col-xs-12",
        ),
        Div(
            Field(
                "precio_compra",
                wrapper_class="input-group input-group-static my-4",
            ),
            css_class="col-lg-2 col-sm-2 col-md-2 col-xs-12",
        ),
        Div(
            Field(
                "precio_venta",
                wrapper_class="input-group input-group-static my-4",
            ),
            css_class="col-lg-2 col-sm-2 col-md-2 col-xs-12",
        ),
    )
    return helper
