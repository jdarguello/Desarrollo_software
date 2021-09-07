from Carrito import CarritoCompras

if __name__ == "__main__":
	productos = {
	    "jeans":{"precio de venta": 200000, "costo de inversion": 120000},
	    "camisa_polo":{"precio de venta": 99000,"costo de inversion": 50000},
	    "vaqueros":{"precio de venta": 220000,"costo de inversion":125000}
	}
	
	carrito = CarritoCompras("juan", productos) #Objeto del carrito del usuario 'juan'

	#Algoritmo interactivo
	while True:
	  art = input("¿Qué artículo deseas comprar? ")
	  cant = int(input("¿Qué cantidad deseas? "))

	  carrito.agregarArticulo(art, cant)

	  if input("¿Deseas eliminar algún artículo? (s/n) ") == "s":
	    carrito.removerArticulo(input("Nombre del artículo: "), int(input("Cantidad: ")))

	  print("El valor acumulado es $" + str(carrito._total))


	  if input("¿Deseas seguir comprando? (s/n) ") == "n":
	    break

	print("Compra finalizada")