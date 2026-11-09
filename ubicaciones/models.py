from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.nombre
