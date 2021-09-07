from Persona import Persona

class Usuario(Persona):
  def __init__(self, nombre, edad, usuario, contraseña=""):
    #Inicialización de atributos
    super().__init__(nombre, edad)  #Inicio de constructor de clase padre
    self.usuario = usuario
    self.contraseña = contraseña
  
  def cambiarContra(self, nueva):
    self.contraseña = nueva