from Persona import Persona

if __name__ == "__main__":
	#Creación de persona
	John = Persona("John Alexander", "jalexander", "123")

	John.addBlog("Robots siglo X", "06/09/2021", "Desde la antiguedad, los robots han existido en otros planetas...")

	print("Blogs de John:", John.blogs, "\n")

	print(John.blogs[0].mostrarBlog())