from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Fieldset, Layout
from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from sisVentas.articulo.models import Articulo


class ArticuloForm(forms.ModelForm):
    """
    Formulario para el modelo Articulo.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.error_text_inline = True
        self.helper.form_id = "formulario-articulo"
        self.helper.form_action = reverse_lazy("articulo:crear_articulo")
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                _("Nuevo Articulo"),
                "categoria",
                Field("codigo", wrapper_class="input-group input-group-static"),
                Field(
                    "nombre",
                    wrapper_class="input-group input-group-static form_dinamic",
                ),
                Field("stock", wrapper_class="input-group input-group-static"),
                Field("descripcion", wrapper_class="input-group input-group-static"),
                Field("imagen", wrapper_class="input-group input-group-static"),
            ),
        )

        campos_select = ["categoria"]
        for select in campos_select:
            self.fields[select].widget.attrs["class"] = "select-form"

    class Meta:
        model = Articulo
        exclude = ["estado"]
