"""
Authors = Julio Ramírez, Eric Ranírez
mantainer = Julio Ramírez
"""

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from core.models import Asistente
from datetime import datetime, date, timedelta
import pytz

FECHAACTUAL = date.today()

# Create your views here.

ticks = 10

fechaInicio = datetime(
    year=FECHAACTUAL.year,
    month=FECHAACTUAL.month,
    day=FECHAACTUAL.day,
    hour=8,
    minute=0,
    second=0,
    tzinfo=pytz.UTC
)

fechafin = datetime(
    year=FECHAACTUAL.year,
    month=FECHAACTUAL.month,
    day=FECHAACTUAL.day,
    hour=22,
    minute=0,
    second=0,
    tzinfo=pytz.UTC
)


class DatosView(TemplateView):
    template_name = 'datos/datos.html'

    def get(self, request, *args, **kwargs):
        asistentes = Asistente.objects.all()
        acreditados = Asistente.objects.filter(validador=True)
        try:
            porcAcreditados = round((acreditados.count() * 100) / asistentes.count())
        except:
            porcAcreditados = 0

        noAcreditados = Asistente.objects.filter(validador=False)
        labels = []
        numeros = [0, 0, 0, 0, 0, 0, 0, 0]

        return render(request, self.template_name, {
            'asistentes': asistentes,
            'acreditados': acreditados,
            'noAcreditados': noAcreditados,
            'porcAcreditados': porcAcreditados,
            'numeros': numeros,
            'etiquetas': labels
        })


def updateDatos(request):
    asistentes = Asistente.objects.all().count()
    acreditados = Asistente.objects.filter(validador=True).count()
    try:
        porcAcreditados = round((acreditados * 100) / asistentes)
    except:
        porcAcreditados = '0%'
    noAcreditados = Asistente.objects.filter(validador=False).count()

    deltaTime = fechafin - fechaInicio
    dias, segundos = deltaTime.days, deltaTime.seconds
    horas = dias * 24 + segundos // 3600

    try:
        rangos = horas / ticks
    except:
        rangos = 1

    labels = []
    numeros = []

    for i in range(ticks):
        numeros.append(0)
        labels.append((fechaInicio + timedelta(hours=rangos * i)).strftime("%d-%m-%y %H:%M"))

    for asis in Asistente.objects.filter(validador=True):
        h = fechaInicio + timedelta(hours=rangos)
        if fechafin >= asis.updated >= fechaInicio:
            for i in range(len(numeros) - 1):
                if asis.updated < h:
                    numeros[i] = numeros[i] + 1
                    break
                else:
                    h = h + timedelta(hours=rangos)

    data = {
        'asistentes': asistentes,
        'acreditados': acreditados,
        'porcAcreditados': porcAcreditados,
        'noAcreditados': noAcreditados,
        'numeros': numeros,
        'etiquetas': labels
    }

    return JsonResponse(data)
