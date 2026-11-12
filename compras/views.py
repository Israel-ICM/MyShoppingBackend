from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from inventarios.services import recibir_compra
from .models import Proveedor, Compra, DetalleCompra
from .serializers import ProveedorSerializer, CompraSerializer, DetalleCompraSerializer, RecibirCompraSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    filterset_fields = ['proveedor', 'estado']

    @action(detail=True, methods=['post'])
    def recibir(self, request, pk=None):
        compra = self.get_object()
        if compra.estado != 'PE':
            return Response(
                {'detail': 'Solo se puede recibir una compra pendiente.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = RecibirCompraSerializer(data=request.data, context={'compra': compra})
        serializer.is_valid(raise_exception=True)
        vencimientos = {
            item['detalle']: item['fecha_vencimiento'] for item in serializer.validated_data['lotes']
        }
        compra = recibir_compra(compra, vencimientos)
        return Response(CompraSerializer(compra).data)


class DetalleCompraViewSet(viewsets.ModelViewSet):
    queryset = DetalleCompra.objects.all()
    serializer_class = DetalleCompraSerializer
    filterset_fields = ['compra']
