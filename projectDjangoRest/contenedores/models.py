from django.db import models
from django.conf import settings

from colaboradores.models import Colaboradores

# Create your models here.
class Contenedor(models.Model):
    responsable = models.ForeignKey(Colaboradores, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del Contenedor',
        unique=True
    )
    barrio = models.CharField(
        max_length=100,
        help_text='Indique el barrio al que va este contenedor',
        unique=True
    )
    fecha_creado = models.DateTimeField()
    vendido = models.BooleanField(default=False)
 
    def __str__(self):
        return '{}'.format(self.descripcion)
 
    class Meta:
        verbose_name_plural = "Contenedores"