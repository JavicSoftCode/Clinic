from  BackEnd.Apps.Auth.models import CustomUser
from django.db import models


class Medicamento(models.Model):
  ESTADOS = (
    ('activo', 'Activo'),
    ('baja', 'De Baja'),
  )

  codigo = models.CharField(max_length=100, unique=True)
  descripcion = models.CharField(max_length=255)
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  stop = models.CharField(null=True, blank=True)
  estado = models.CharField(max_length=10, choices=ESTADOS, default='activo')
  usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.descripcion} ({self.codigo})'
