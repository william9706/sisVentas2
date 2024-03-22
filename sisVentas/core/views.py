from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from sisVentas.core.forms import PerfilPersonaForm
from sisVentas.core.models import PerfilPersona

User = get_user_model()


class PerfilPersonaListView(LoginRequiredMixin, ListView):
    model = PerfilPersona
    context_object_name = "personas"
    template_name = "persona/listar_personas.html"
    paginate_by = 15


class PerfilPersonaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Vista para crear una persona.
    """

    model = PerfilPersona
    form_class = PerfilPersonaForm
    template_name = "persona/crear_persona.html"
    success_url = reverse_lazy("persona:listar_personas")
    success_message = _("Persona creada exitosamente.")


class PerfilPersonaUpdateview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Vista para actualizar persona
    """

    model = PerfilPersona
    form_class = PerfilPersonaForm
    template_name = "persona/crear_persona.html"
    success_url = reverse_lazy("persona:listar_personas")
    success_message = _("Persona actualizada correctamente.")


class PerfilPersonaDeleteview(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Vista para eliminar una persona.
    """

    model = PerfilPersona
    success_message = _("Persona eliminada correctamente.")
    template_name = "persona/eliminar_persona.html"
    success_url = reverse_lazy("persona:listar_personas")


class UserDetailView(LoginRequiredMixin, DetailView):
    """
    Vista para listar un perfil específico.
    """
    model = User
    slug_field = "pk"
    context_object_name = "user"
