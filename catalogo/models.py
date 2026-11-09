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
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=149)
    descripcion = models.TextField()
    pais_id = models.ForeignKey(
        Pais,
        on_delete=models.PROTECT,
        related_name='productos'
    )
    marca_id = models.ForeignKey(
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
