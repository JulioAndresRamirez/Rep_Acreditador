from django.db import models

# Create your models here.

'''
class Evento(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')
    lugar = models.CharField(max_length=200,null=True, blank=True, verbose_name='Lugar')
    fecha = models.DateField(null=True, blank=True, verbose_name='Fecha del evento')
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-created']

    def __str__(self):
        return self.titulo

'''
