from rest_framework import serializers
from .models import MovimientoStock, LoteInventario


class MovimientoStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoStock
        fields = "__all__"


class LoteInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteInventario
        fields = "__all__"
