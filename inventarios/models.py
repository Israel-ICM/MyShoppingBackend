from django.db import models
from catalogo.models import Producto

class TipoMovimiento(models.TextChoices):
    VENTA = "VT", "Venta"
    COMPRA = "CM", "Compra"
    AJUSTE = "AJ", "Ajuste"
    DEVOLUCION = "DV", "Devolución"
    MERMA = "MR", "Merma"


class MovimientoStock(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name="movimientos_stock"
    )
    tipo = models.CharField(max_length=2, choices=TipoMovimiento.choices)
    cantidad = models.IntegerField()
    stock_resultante = models.PositiveIntegerField()
    creado_en = models.DateTimeField(auto_now_add=True)
