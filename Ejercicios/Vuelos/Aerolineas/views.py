from rest_framework import viewsets

from Aerolineas.serializers import *

class AerolineaAPI (viewsets.ModelViewSet):
    serializer_class = AerolineaSerial
    queryset = Aerolinea.objects.all()

class AvionAPI (viewsets.ModelViewSet):
    serializer_class = AvionSerial
    queryset = Avion.objects.all()
    #queryset => información que se desea enviar al frontend

class VueloAPI (viewsets.ModelViewSet):
    serializer_class = VueloSerial
    queryset = Vuelo.objects.all()