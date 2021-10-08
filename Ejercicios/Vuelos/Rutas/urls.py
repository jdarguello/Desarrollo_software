#Gestión de direcciones locales de 'Rutas'

from django.urls import path, include   #Organizamos las direcciones locales
from rest_framework.routers import DefaultRouter    #=> Organizar direcciones de ViewSets

from Rutas.views import *

router = DefaultRouter()
router.register('aeropuertos', AeropuertoAPI)
router.register('rutas', RutaAPI)

urlpatterns =[
    #Organiza las direcciones locales
    path('crud/', include(router.urls))
]
