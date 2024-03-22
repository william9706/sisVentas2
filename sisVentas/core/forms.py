from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Fieldset, Layout
from django import forms
from django.utils.translation import gettext_lazy as _

from sisVentas.core.models import PerfilPersona


class PerfilPersonaForm(forms.ModelForm):
    """
    Formulario para vista PerfilPersonaCreateview.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_id = "formulario-persona"
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                _("Nueva Persona"),
                "tipo_persona",
                Field("nombre_persona", wrapper_class="input-group input-group-static"),
                "tipo_persona",
                Field(
                    "numero_docuento", wrapper_class="input-group input-group-static"
                ),
                Field("direccion", wrapper_class="input-group input-group-static"),
                Field("telefono", wrapper_class="input-group input-group-static"),
                Field("email", wrapper_class="input-group input-group-static"),
            )
        )

        campos_select = ["tipo_persona", "tipo_persona"]
        for field in campos_select:
            self.fields[field].widget.attrs["class"] = "select-form"

    class Meta:
        model = PerfilPersona
        fields = "__all__"
