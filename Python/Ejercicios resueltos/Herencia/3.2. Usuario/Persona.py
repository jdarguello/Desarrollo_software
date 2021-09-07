class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  
  def descripcion(self):
    return self.nombre + " tiene " + str(self.edad) + " años."