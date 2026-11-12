from rest_framework import serializers
from .models import MovimientoStock, LoteInventario

TIPOS_AJUSTE_MANUAL = ["AJ", "DV", "MR"]


class MovimientoStockSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source="producto.nombre", read_only=True)

    class Meta:
        model = MovimientoStock
        fields = "__all__"
        read_only_fields = ["stock_resultante"]


class LoteInventarioSerializer(serializers.ModelSerializer):
    producto = serializers.IntegerField(source="detalle_compra.producto_id", read_only=True)
    producto_nombre = serializers.CharField(source="detalle_compra.producto.nombre", read_only=True)

    class Meta:
        model = LoteInventario
        fields = "__all__"


class AjusteStockSerializer(serializers.Serializer):
    producto = serializers.IntegerField()
    tipo = serializers.ChoiceField(choices=TIPOS_AJUSTE_MANUAL)
    cantidad = serializers.IntegerField()
    observacion = serializers.CharField(required=False, allow_blank=True, default="")

    def validate_cantidad(self, value):
        if value == 0:
            raise serializers.ValidationError("La cantidad no puede ser cero.")
        return value
