from django.views.generic import ListView

from sisVentas.core.models import PerfilPersona


class PerfilPersonaListView(ListView):
    model = PerfilPersona
    context_object_name = "personas"
    template_name = "personas/perfil_personas.html"
    paginate_by = 15
