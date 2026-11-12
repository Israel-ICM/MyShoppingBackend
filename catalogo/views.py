from django.core.files.storage import default_storage
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Categoria, Marca, Producto
from .serializers import CategoriaSerializer, MarcaSerializer, ProductoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filterset_fields = ['categorias', 'marca', 'activo']
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['post'], parser_classes=[MultiPartParser, FormParser])
    def subir_imagen(self, request):
        archivo = request.FILES.get('archivo')
        if not archivo:
            return Response({'detail': 'Falta el archivo.'}, status=400)
        ruta = default_storage.save(f'productos/{archivo.name}', archivo)
        url = request.build_absolute_uri(default_storage.url(ruta))
        return Response({'url': url})
