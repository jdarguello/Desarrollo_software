from django.db import models
from django.contrib.auth import get_user_model

from Productos.models import Producto

class CarritoCompras(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.usuario) + " - " + str(self.fecha)

    @property
    def total(self):
        total = 0
        for articulo in self.articulo_set.all():
            total += articulo.subtotal()
        return total

class Articulo(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.carrito.__str__() + " / " + self.producto.nombre
    
    def subtotal(self):
        return self.producto.precio*self.cantidad

class InfoEnvio(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    pais = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

    def __str__(self):
        return self.carrito.__str__()