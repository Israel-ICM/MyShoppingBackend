from rest_framework import serializers
from .models import Categoria, Marca, Producto, ProductoFoto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"


class ProductoFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoFoto
        fields = ["id", "url", "principal"]


class ProductoSerializer(serializers.ModelSerializer):
    marca_nombre = serializers.CharField(source="marca.nombre", read_only=True)
    fotos = ProductoFotoSerializer(source="fotos_producto", many=True, read_only=True)

    class Meta:
        model = Producto
        fields = "__all__"
