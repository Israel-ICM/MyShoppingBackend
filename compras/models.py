from django.db import models
from catalogo.models import Producto

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    web = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre


class EstadoCompra(models.TextChoices):
    PENDIENTE = "PE", "Pendiente"
    RECIBIDA = "RC", "Recibida"
    CANCELADA = "CA", "Cancelada"


class Compra(models.Model):
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT,
        related_name="compras"
    )
    estado = models.CharField(
        max_length=2,
        choices=EstadoCompra.choices,
        default=EstadoCompra.PENDIENTE
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Compra #{self.pk} - {self.proveedor.nombre}"


class DetalleCompra(models.Model):
    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name="detalles"
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name="detalles_compra"
    )
    cantidad = models.PositiveIntegerField(default=1)
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'compras_detalle'

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
