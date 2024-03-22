from django.urls import path

from sisVentas.core.views import (
    PerfilPersonaCreateView,
    PerfilPersonaDeleteview,
    PerfilPersonaListView,
    PerfilPersonaUpdateview,
    UserDetailView,
)

app_name = "persona"
urlpatterns = [
    path("listar-personas/", PerfilPersonaListView.as_view(), name="listar_personas"),
    path("nueva-persona/", PerfilPersonaCreateView.as_view(), name="crear_persona"),
    path(
        "actualizar-persona/<str:pk>/",
        PerfilPersonaUpdateview.as_view(),
        name="actualizar_persona",
    ),
    path(
        "eliminar-persona/<str:pk>/",
        PerfilPersonaDeleteview.as_view(),
        name="eliminar_persona",
    ),
    path("profile/<str:pk>/", UserDetailView.as_view(), name="profile"),
]
