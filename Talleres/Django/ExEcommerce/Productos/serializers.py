#Creamos los serializadores de nuestra aplicación

#Serializadores => convertir en diccionarios Python
# los objetos CRUD

from rest_framework import serializers

from Productos.models import *

class TipoSerial(serializers.ModelSerializer):
    class Meta:
        model = TipoElectrodomestico
        fields = '__all__'
        #fields = ["nombre", "foto"]

class ProductoSerial(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "descripcion", "marca", "ref", "tipoEl"]
