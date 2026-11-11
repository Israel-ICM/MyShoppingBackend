from django.db import transaction
from rest_framework import serializers
from .models import Pedido, DetallePedido


class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = "__all__"


class DetallePedidoInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ["id", "producto", "cantidad", "precio_unitario"]
        read_only_fields = ["id"]


class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoInlineSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ["id", "cliente", "fecha", "observacion", "estado", "total", "detalles"]
        read_only_fields = ["fecha", "total"]

    def create(self, validated_data):
        detalles_data = validated_data.pop("detalles")
        with transaction.atomic():
            pedido = Pedido.objects.create(**validated_data)
            for detalle in detalles_data:
                DetallePedido.objects.create(pedido=pedido, **detalle)
        return pedido
