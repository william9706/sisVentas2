from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from sisVentas.articulo.api.serializers import ArticuloSerializer
from sisVentas.articulo.models import Articulo


class ArticulosViewSet(ModelViewSet):
    """
    endpoint para gestionar articulos.
    """

    permission_classes = [IsAuthenticated]
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
