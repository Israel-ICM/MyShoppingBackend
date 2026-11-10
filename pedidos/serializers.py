from rest_framework import serializers
from .models import Pedido, DetallePedido


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"


class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = "__all__"
