from rest_framework import serializers
from .models import Categoria, Marca, Producto, ProductoFoto, ProductoVideo


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"


class ProductoFotoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProductoFoto
        fields = ["id", "url", "principal"]


class ProductoVideoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProductoVideo
        fields = ["id", "url"]


class ProductoSerializer(serializers.ModelSerializer):
    marca_nombre = serializers.CharField(source="marca.nombre", read_only=True)
    fotos = ProductoFotoSerializer(source="fotos_producto", many=True, required=False)
    videos = ProductoVideoSerializer(source="videos_producto", many=True, required=False)

    class Meta:
        model = Producto
        fields = "__all__"

    def create(self, validated_data):
        fotos_data = validated_data.pop("fotos_producto", [])
        videos_data = validated_data.pop("videos_producto", [])
        producto = super().create(validated_data)
        for foto in fotos_data:
            ProductoFoto.objects.create(producto=producto, **foto)
        for video in videos_data:
            ProductoVideo.objects.create(producto=producto, **video)
        return producto

    def update(self, instance, validated_data):
        fotos_data = validated_data.pop("fotos_producto", None)
        videos_data = validated_data.pop("videos_producto", None)
        instance = super().update(instance, validated_data)
        if fotos_data is not None:
            instance.fotos_producto.all().delete()
            for foto in fotos_data:
                ProductoFoto.objects.create(producto=instance, **foto)
        if videos_data is not None:
            instance.videos_producto.all().delete()
            for video in videos_data:
                ProductoVideo.objects.create(producto=instance, **video)
        return instance
