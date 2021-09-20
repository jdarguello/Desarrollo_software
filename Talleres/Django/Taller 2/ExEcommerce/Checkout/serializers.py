from rest_framework import serializers
from Checkout.models import *

class CarritoSerial (serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras
        fields = ['usuario', 'fecha', 'total']

class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class InfoEnvioSerial(serializers.ModelSerializer):
    class Meta:
        model = InfoEnvio
        fields = '__all__'
