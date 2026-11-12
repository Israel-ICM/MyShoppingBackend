from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=150)
    abreviacion = models.CharField(max_length=10, blank=True)
    def __str__(self) -> str:
        return self.nombre

class Region(models.Model):
    nombre = models.CharField(max_length=150)
    abreviacion = models.CharField(max_length=10, blank=True)
    pais = models.ForeignKey(
        Pais,
        on_delete=models.PROTECT,
        related_name='regiones'
    )
    def __str__(self) -> str:
        return self.nombre
