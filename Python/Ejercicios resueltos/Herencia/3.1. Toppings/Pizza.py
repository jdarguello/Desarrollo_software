from MasaBase import MasaBase

class Pizza(MasaBase):
  def __init__(self, nombre, tamaño, saborMB, precioVenta, costoMB, toppings = []):
    super().__init__(tamaño, costoMB, saborMB)  #Inicializar el constructor de la masa base
    #Inicializar atributos
    self.nombre = nombre
    self.precio = precioVenta
    self.toppings = toppings

    self.costoFinal() #Accede al método 'costoFinal' y calcula el precio final de la pizza
  
  def costoFinal(self):
    for topping in self.toppings:
      self.costo += topping.costo
    
  def utilidadBruta(self):
    return self.precio - self.costo
  
  def descripcion(self):
    infoToppings = "Tiene: "
    for topping in self.toppings:
      infoToppings += topping.nombre  + ", "
    infoToppings = infoToppings[:-2] + "."
    return "Información de los ingredientes de la pizza: " + super().descripcion() + infoToppings \
           + "\nLa pizza de " + self.nombre + " cuesta $" + str(self.costo) + " y tiene una utilidad bruta de $" + str(self.utilidadBruta())