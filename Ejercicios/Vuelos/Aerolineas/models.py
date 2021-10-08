from django.db import models

# Create your models here.

from Rutas.models import Ruta 

class Aerolinea (models.Model):
    nombre = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, null=True)
    paisPrincipal = models.CharField(max_length=200)
    ubicacionSede = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Avion (models.Model):
    numRegistro = models.CharField(max_length=300, primary_key=True)
    asienstosEcon = models.IntegerField(default=0)
    asientosEje = models.IntegerField(default=0)
    capCombustible = models.FloatField(default=0)
    marca = models.CharField(max_length=200)
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.CASCADE)
    velocidad = models.FloatField(default=0)


    def __str__(self):
        return self.aerolinea.__str__() + " / " + self.numRegistro
    
    @property
    def capacidadPasajeros(self):
        return self.asienstosEcon + self.asientosEje

class Vuelo(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.SET_NULL, null=True)
    ruta = models.ForeignKey(Ruta, on_delete=models.SET_NULL, null=True)
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.CASCADE)
    precioEcon = models.FloatField(default=0)
    precioEje = models.FloatField(default=0)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.aerolinea.__str__() + " / " + self.ruta.__str__() + " / " + self.fecha
    
    @property
    def duracion(self):
        #velocidad = distancia/tiempo => tiempo = distancia/velocidad
        pass

    @property   #=> conierte un método en un atributo -> permite enviarlo a la API a través del serializador
    def asientosEcon(self):
        pass

    @property
    def asientosEje(self):
        pass