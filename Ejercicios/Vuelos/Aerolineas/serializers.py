from rest_framework import serializers

from Aerolineas.models import *

#serialización => Objeto Python -> diccionario Python -> JSON

#deserialización => JSON -> diccionario Python -> Objeto Python


class AerolineaSerial(serializers.ModelSerializer):
    class Meta:
        #=> Permite cambiar el comportamiento normal (naturaleza -> 'abstractas') de una clase 
        model = Aerolinea
        fields = '__all__'

class AvionSerial (serializers.ModelSerializer):
    class Meta:
        model = Avion
        fields = '__all__'

class VueloSerial (serializers.ModelSerializer):
    class Meta:
        model = Vuelo
        fields = '__all__'
