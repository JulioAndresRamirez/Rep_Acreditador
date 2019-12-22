from django.db import models


# Create your models here.

class Asistente(models.Model):
    identificador = models.CharField(max_length=12, verbose_name='Numero Identificador')
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    apellido = models.CharField(max_length=256, verbose_name='Apellido')
    email = models.EmailField(null=True, blank=True)
    validador = models.BooleanField(default=False, verbose_name='Estado acreditacion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')

    class Meta:
        verbose_name = 'Asistente'
        verbose_name_plural = 'Asistentes'
        ordering = ['nombre', 'validador']

    def __str__(self):
        return self.nombre



