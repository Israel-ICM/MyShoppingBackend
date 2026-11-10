from django.db import models
from catalogo.models import Producto
from compras.models import DetalleCompra

class TipoMovimiento(models.TextChoices):
    VENTA = "VT", "Venta"
    COMPRA = "CM", "Compra"
    AJUSTE = "AJ", "Ajuste"
    DEVOLUCION = "DV", "Devolución"
    MERMA = "MR", "Merma"


class LoteInventario(models.Model):
    detalle_compra = models.OneToOneField(
        DetalleCompra,
        on_delete=models.PROTECT,
        related_name="lote"
    )
    fecha_vencimiento = models.DateField()
    cantidad_actual = models.PositiveIntegerField()
    creado_en = models.DateTimeField(auto_now_add=True)


class MovimientoStock(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name="movimientos_stock"
    )
    tipo = models.CharField(max_length=2, choices=TipoMovimiento.choices)
    cantidad = models.IntegerField()
    stock_resultante = models.PositiveIntegerField()
    lote = models.ForeignKey(
        LoteInventario,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="movimientos"
    )
    creado_en = models.DateTimeField(auto_now_add=True)
