from django.urls import include, path
from rest_framework.routers import DefaultRouter

from sisVentas.articulo.api.views import ArticulosViewSet

router = DefaultRouter()
router.register("articulo", ArticulosViewSet)

app_name = "api_articulo"
urlpatterns = [
    path("", include(router.urls)),
]
