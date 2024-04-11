from rest_framework import serializers

from sisVentas.articulo.models import Articulo


class ArticuloSerializer(serializers.ModelSerializer):
    """
    Serializzador para modelo articulo.
    """

    class Meta:
        model = Articulo
        fields = "__all__"
