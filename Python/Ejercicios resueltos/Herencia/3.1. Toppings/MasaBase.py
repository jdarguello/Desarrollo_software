class MasaBase:
  def __init__(self, tamaño, costo, sabor):
    #Inicializar los atributos
    self.tamaño = tamaño
    self.costo = costo
    self.sabor = sabor
  
  def descripcion(self):
    return "La masa base es de " + self.sabor + " y tiene un tamaño de " + str(self.tamaño) + " cm. "