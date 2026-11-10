from rest_framework import viewsets

from .models import MovimientoStock, LoteInventario
from .serializers import MovimientoStockSerializer, LoteInventarioSerializer


class MovimientoStockViewSet(viewsets.ModelViewSet):
    queryset = MovimientoStock.objects.all()
    serializer_class = MovimientoStockSerializer


class LoteInventarioViewSet(viewsets.ModelViewSet):
    queryset = LoteInventario.objects.all()
    serializer_class = LoteInventarioSerializer
