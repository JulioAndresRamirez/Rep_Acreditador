from django.urls import path
from .views import index, UpdateAsistente, SearchAsistente

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('acreditar/<pk>', UpdateAsistente.as_view(), name='acreditar'),
    path('busqueda', SearchAsistente.as_view(), name='busqueda'),
]
