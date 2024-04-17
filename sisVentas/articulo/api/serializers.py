from rest_framework import serializers

from sisVentas.articulo.models import Articulo, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    """
    Serializador para modelo categoria.
    """

    class Meta:
        model = Categoria
        fields = "__all__"


class ArticuloSerializer(serializers.ModelSerializer):
    """
    Serializzador para modelo articulo.
    """

    class Meta:
        model = Articulo
        fields = "__all__"
