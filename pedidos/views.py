from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Pedido, DetallePedido
from .serializers import PedidoSerializer, DetallePedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filterset_fields = ['cliente', 'estado']

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

    def perform_create(self, serializer):
        pedido = serializer.save()
        if pedido.cliente.email:
            send_mail(
                subject="Confirmacion de tu pedido - MyShopping",
                message=f"Hola {pedido.cliente.nombre}, recibimos tu pedido #{pedido.id}. Total: Bs {pedido.total}.",
                from_email=None,
                recipient_list=[pedido.cliente.email],
                fail_silently=True,
            )


class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    filterset_fields = ['pedido']
