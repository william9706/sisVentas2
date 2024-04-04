from rest_framework.viewsets import ModelViewSet

from sisVentas.articulo.models import Articulo


class ArticulosViewSet(ModelViewSet):
    queryset = Articulo.objects.all()
