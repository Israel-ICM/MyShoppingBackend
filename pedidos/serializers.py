from django.db import transaction
from rest_framework import serializers
from cuentas.models import Cliente
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


class ClientePedidoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=200)
    telefono = serializers.CharField(max_length=20)
    email = serializers.EmailField(required=False, allow_blank=True)


class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoInlineSerializer(many=True)
    cliente = ClientePedidoSerializer()

    class Meta:
        model = Pedido
        fields = ["id", "cliente", "region", "fecha", "observacion", "estado", "total", "detalles"]
        read_only_fields = ["fecha", "total"]

    def create(self, validated_data):
        detalles_data = validated_data.pop("detalles")
        cliente_data = validated_data.pop("cliente")
        with transaction.atomic():
            cliente, _ = Cliente.objects.get_or_create(
                telefono=cliente_data["telefono"],
                defaults={
                    "nombre": cliente_data["nombre"],
                    "email": cliente_data.get("email", ""),
                },
            )
            pedido = Pedido.objects.create(cliente=cliente, **validated_data)
            for detalle in detalles_data:
                DetallePedido.objects.create(pedido=pedido, **detalle)
        return pedido
