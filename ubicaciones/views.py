from rest_framework import viewsets

from .models import Pais
from .serializers import PaisSerializer


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
