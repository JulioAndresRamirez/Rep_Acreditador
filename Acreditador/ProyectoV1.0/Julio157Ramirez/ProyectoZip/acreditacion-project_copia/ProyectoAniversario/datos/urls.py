from django.urls import path
from .views import DatosView, updateDatos

urlpatterns = [
    path('datos/', DatosView.as_view(), name='datos'),
    path('ajax/updateDatos/', updateDatos, name='updateDatos'),
]
