from django.db import transaction
from rest_framework import serializers
from .models import Proveedor, Compra, DetalleCompra


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"


class DetalleCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields = "__all__"


class DetalleCompraInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields = ["id", "producto", "cantidad", "costo_unitario"]
        read_only_fields = ["id"]


class CompraSerializer(serializers.ModelSerializer):
    detalles = DetalleCompraInlineSerializer(many=True)

    class Meta:
        model = Compra
        fields = ["id", "proveedor", "estado", "creado_en", "detalles"]
        read_only_fields = ["creado_en"]

    def create(self, validated_data):
        detalles_data = validated_data.pop("detalles")
        with transaction.atomic():
            compra = Compra.objects.create(**validated_data)
            for detalle in detalles_data:
                DetalleCompra.objects.create(compra=compra, **detalle)
        return compra


class LoteVencimientoSerializer(serializers.Serializer):
    detalle = serializers.IntegerField()
    fecha_vencimiento = serializers.DateField()


class RecibirCompraSerializer(serializers.Serializer):
    lotes = LoteVencimientoSerializer(many=True)

    def validate_lotes(self, value):
        compra = self.context["compra"]
        ids_detalles = set(compra.detalles.values_list("id", flat=True))
        ids_recibidos = {item["detalle"] for item in value}
        if ids_detalles != ids_recibidos:
            raise serializers.ValidationError(
                "Debes indicar la fecha de vencimiento de cada linea de la compra."
            )
        return value
