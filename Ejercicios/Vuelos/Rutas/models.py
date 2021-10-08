from django.db import models

# Base del proyecto - conexión CRUD

class Aeropuerto(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)

    def __str__(self):
        #especifica identificación de objetos
        return self.nombre + " - " + self.pais

class Ruta (models.Model):
    origen = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, related_name="+")
    destino = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, related_name="+")
    disancia = models.FloatField(default=0)

    def __str__(self):
        return self.origen.__str__() + " / " + self.destino.__str__()