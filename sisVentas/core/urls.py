from django.urls import path

from sisVentas.core.views import PerfilPersonaListView

app_name = "persona"
urlpatterns = [
    path("listar-personas/", PerfilPersonaListView.as_view(), name="listar_personas")
]
