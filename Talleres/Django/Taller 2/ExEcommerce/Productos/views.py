from rest_framework import viewsets
from rest_framework.status import HTTP_400_BAD_REQUEST

from Productos.serializers import *

class TipoAPI (viewsets.ModelViewSet):
    serializer_class = TipoSerial
    #queryset => objetos que queremos enviar al frontend
    queryset = TipoElectrodomestico.objects.all()

class ProductoAPI (viewsets.ModelViewSet):
    serializer_class = ProductoSerial
    #queryset => objetos que queremos enviar al frontend
    queryset = Producto.objects.all()

class ComentarioAPI(viewsets.ModelViewSet):
    serializer_class = ComentarioSerial
    queryset = Comentario.objects.all()