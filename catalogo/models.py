from django.db import models
from ubicaciones.models import Pais

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    categorias = models.ManyToManyField(Categoria, related_name='productos')
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    pais = models.ForeignKey(
        Pais,
        on_delete=models.PROTECT,
        related_name='productos'
    )
    marca = models.ForeignKey(
        Marca,
        on_delete=models.PROTECT,
        related_name='productos'
    )
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    link_referencia = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombre

class ProductoVideo(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='videos_producto'
    )
    url = models.CharField(max_length=255)

    class Meta:
        db_table = 'catalogo_producto_video'

class ProductoFoto(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='fotos_producto'
    )
    url = models.CharField(max_length=255)
    principal = models.BooleanField(default=False)

    class Meta:
        db_table = 'catalogo_producto_foto'


class HistorialPrecio(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name="historial_precios"
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    vigente_desde = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'catalogo_historial_precio'

    @property
    def margen_sobre_costo(self):
        return (self.precio - self.costo) / self.costo * 100

    @property
    def margen_bruto(self):
        return (self.precio - self.costo) / self.precio * 100
