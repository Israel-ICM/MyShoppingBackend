from django.db import models
from catalogo.models import Producto
from cuentas.models import Cliente
from ubicaciones.models import Region

class EstadoPedido(models.TextChoices):
    PENDIENTE = "PE", "Pendiente"
    CONFIRMADO = "CO", "Confirmado"
    ENVIADO = "EN", "Enviado"
    ENTREGADO = "EG", "Entregado"
    CANCELADO = "CA", "Cancelado"


class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='pedidos'
    )
    fecha = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        related_name='pedidos',
        null=True,
        blank=True,
    )
    observacion = models.CharField(max_length=255, blank=True)
    estado = models.CharField(
        max_length=2,
        choices=EstadoPedido.choices,
        default=EstadoPedido.PENDIENTE
    )
    @property
    def total(self):
        return sum(d.cantidad * d.precio_unitario for d in self.detalles.all()) # pyright: ignore[reportAttributeAccessIssue]


class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='detalles_pedido'
    )
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'pedidos_detalle'

    def __str__(self) -> str:
        return f"{self.cantidad} x {self.producto.nombre}"
