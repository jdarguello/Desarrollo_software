from django.db.models import fields
from rest_framework import serializers

#Serializador => objeto Python -> diccionario -> JSON

from Productos.models import *


class TipoSerial (serializers.ModelSerializer):
    class Meta:
        #Metaclase => flexibiliza la forma en cómo se emplean los métodos y atributos de un clase
        model = TipoElectrodomestico
        fields = '__all__'
        #fields = ['nombre', "foto"]


class ProductoSerial (serializers.ModelSerializer):
    class Meta:
        #Metaclase => flexibiliza la forma en cómo se emplean los métodos y atributos de un clase
        model = Producto
        #fields = '__all__'
        fields = ['nombre', "foto", "tipo", "descripcion", "calcularCalificacion", "marca", "ref"]

class ComentarioSerial(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'