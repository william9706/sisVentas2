from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from sisVentas.articulo.api.custom_permissions import ClienteRequestPermission
from sisVentas.articulo.api.serializers import ArticuloSerializer
from sisVentas.articulo.models import Articulo


class ArticulosViewSet(ModelViewSet):
    """
    endpoint para gestionar articulos.
    """

    permission_classes = [IsAuthenticated, ClienteRequestPermission]
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    authentication_classes = [JWTAuthentication]
