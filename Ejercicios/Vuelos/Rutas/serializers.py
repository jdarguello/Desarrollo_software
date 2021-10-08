#Creamos serializadores de modelos CRUD

from rest_framework import serializers

from Rutas.models import *

class AeropuertoSerial(serializers.ModelSerializer):
    class Meta:
        model = Aeropuerto
        fields = '__all__'

class RutaSerial (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'