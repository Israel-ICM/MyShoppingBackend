from django.db import models
from pedidos.models import Pedido


class MetodoPago(models.TextChoices):
    TARJETA = "TC", "Tarjeta"
    TRANSFERENCIA = "TR", "Transferencia"
    EFECTIVO = "EF", "Efectivo"


class EstadoPago(models.TextChoices):
    PENDIENTE = "PE", "Pendiente"
    COMPLETADO = "CO", "Completado"
    FALLIDO = "FA", "Fallido"
    REEMBOLSADO = "RE", "Reembolsado"


class Pago(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.PROTECT,
        related_name="pagos"
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=2, choices=MetodoPago.choices)
    estado = models.CharField(max_length=2, choices=EstadoPago.choices, default=EstadoPago.PENDIENTE)
    referencia_externa = models.CharField(max_length=100, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago #{self.pk} - {self.pedido} - {self.get_estado_display()}" # pyright: ignore[reportAttributeAccessIssue]
