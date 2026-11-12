from rest_framework import serializers
from .models import Pago


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = "__all__"
        extra_kwargs = {"estado": {"default": "CO"}}

    def validate(self, attrs):
        pedido = attrs.get("pedido") or getattr(self.instance, "pedido", None)
        monto = attrs.get("monto", getattr(self.instance, "monto", None))
        estado = attrs.get("estado", getattr(self.instance, "estado", "CO"))

        if pedido and pedido.estado == "CA":
            raise serializers.ValidationError("No se puede registrar un pago para un pedido cancelado.")

        if pedido and estado == "CO" and monto is not None:
            saldo = pedido.saldo_pendiente
            if self.instance and self.instance.estado == "CO":
                saldo += self.instance.monto
            if monto > saldo:
                raise serializers.ValidationError(
                    f"El monto (Bs {monto}) supera el saldo pendiente del pedido (Bs {saldo})."
                )
        return attrs
