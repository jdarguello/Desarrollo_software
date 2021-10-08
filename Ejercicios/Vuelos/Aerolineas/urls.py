#Gestión de direcciones locales de la apliación 'Aerolíneas'

from django.urls import path, include
from rest_framework import urlpatterns   #=> gestión de direcciones

from rest_framework.routers import DefaultRouter    #=> direcciones tipo ViewSet (API's)

from Aerolineas.views import *

router = DefaultRouter()
router.register('aerolineas', AerolineaAPI)
router.register('aviones', AvionAPI)
router.register('vuelos', VueloAPI)

urlpatterns = [
    #Inscripción de direcciones locales
    path('crud/', include(router.urls))
]