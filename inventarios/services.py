from django.db import transaction
from catalogo.models import Producto
from .models import MovimientoStock, LoteInventario


def registrar_movimiento(producto_id, tipo, cantidad, lote=None, observacion=""):
    """Registra un movimiento de stock y actualiza Producto.stock de forma atomica.
    cantidad positiva = entrada, negativa = salida. stock_resultante se calcula siempre aqui,
    nunca se confia en un valor mandado por el cliente."""
    with transaction.atomic():
        producto = Producto.objects.select_for_update().get(pk=producto_id)
        nuevo_stock = producto.stock + cantidad
        producto.stock = nuevo_stock
        producto.save(update_fields=["stock"])
        return MovimientoStock.objects.create(
            producto=producto,
            tipo=tipo,
            cantidad=cantidad,
            stock_resultante=nuevo_stock,
            lote=lote,
            observacion=observacion,
        )


def recibir_compra(compra, vencimientos_por_detalle):
    """vencimientos_por_detalle: dict {detalle_id: fecha_vencimiento}. Crea un lote y un
    movimiento COMPRA por cada detalle de la compra."""
    with transaction.atomic():
        for detalle in compra.detalles.all():
            fecha_vencimiento = vencimientos_por_detalle[detalle.id]
            lote = LoteInventario.objects.create(
                detalle_compra=detalle,
                fecha_vencimiento=fecha_vencimiento,
                cantidad_actual=detalle.cantidad,
            )
            registrar_movimiento(
                producto_id=detalle.producto_id,
                tipo="CM",
                cantidad=detalle.cantidad,
                lote=lote,
                observacion=f"Compra #{compra.id}",
            )
        compra.estado = "RC"
        compra.save(update_fields=["estado"])
    return compra
