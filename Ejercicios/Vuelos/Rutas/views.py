from rest_framework import viewsets

from Rutas.serializers import *

class AeropuertoAPI(viewsets.ModelViewSet):
    serializer_class = AeropuertoSerial
    queryset = Aeropuerto.objects.all()

class RutaAPI(viewsets.ModelViewSet):
    serializer_class = RutaSerial
    queryset = Ruta.objects.all()