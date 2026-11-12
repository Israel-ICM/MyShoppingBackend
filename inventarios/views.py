from rest_framework import viewsets
from rest_framework.response import Response

from .models import MovimientoStock, LoteInventario
from .serializers import AjusteStockSerializer, MovimientoStockSerializer, LoteInventarioSerializer
from .services import registrar_movimiento


class MovimientoStockViewSet(viewsets.ModelViewSet):
    queryset = MovimientoStock.objects.all()
    serializer_class = MovimientoStockSerializer
    filterset_fields = ['producto', 'tipo']

    def create(self, request, *args, **kwargs):
        serializer = AjusteStockSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movimiento = registrar_movimiento(
            producto_id=serializer.validated_data['producto'],
            tipo=serializer.validated_data['tipo'],
            cantidad=serializer.validated_data['cantidad'],
            observacion=serializer.validated_data['observacion'],
        )
        return Response(MovimientoStockSerializer(movimiento).data, status=201)


class LoteInventarioViewSet(viewsets.ModelViewSet):
    queryset = LoteInventario.objects.all()
    serializer_class = LoteInventarioSerializer
