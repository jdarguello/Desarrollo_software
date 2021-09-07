class CarritoCompras:
  def __init__(self, usuario, productosBD):
    #Inicializamos atributos -> no sólo caracterizan un objeto, sino que además se tratan como variables globales dentro del objeto
    self.usuario = usuario
    self.listaCompras = {}
    self.productos = productosBD
    self._total = 0
  
  def agregarArticulo(self, nombreArt, cant):
    #Existe la posibilidad de que el artículo ya exista

    if nombreArt in self.listaCompras:
      #Artículo ya existe
      self.listaCompras[nombreArt] += cant
    else:
      #No existe
      self.listaCompras[nombreArt] = cant

    self.total(nombreArt, cant)

  def removerArticulo(self, nombreArt, cant):
    #¿La cantidad a remover es mayor que la cantidad existente?
    if cant >= self.listaCompras[nombreArt]:
      #Cantidad a eliminar es mayor que la que existe en la lista de compras
      self.total(nombreArt, self.listaCompras[nombreArt], operador=-1)
      del self.listaCompras[nombreArt]
    else:
      self.listaCompras[nombreArt] -= cant
      self.total(nombreArt, cant, operador=-1)

  def total(self, art, cant, operador=1):
    precioUnitarioArt = self.productos[art]['precio de venta']
    subtotal = cant*precioUnitarioArt
    self._total += operador*subtotal