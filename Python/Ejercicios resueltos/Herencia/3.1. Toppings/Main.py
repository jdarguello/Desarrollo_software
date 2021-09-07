from Toppings import Topping
from Pizza import Pizza

if __name__ == "__main__":
	#Toppings
	tomate = Topping("Tomate", 500, 50)
	queso = Topping("Queso", 300, 100)
	Salami = Topping("Salami", 600, 150)

	#Pizza
	pizzaSalami = Pizza("Salami", 15, "Harina", 8000, 500, [tomate, queso, Salami])

	print(pizzaSalami.descripcion())
	