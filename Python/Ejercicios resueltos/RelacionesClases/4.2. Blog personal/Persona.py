from Blog import Blog

class Persona:
	def __init__(self, nombre, usuario, contraseña, edad=0, nivelEducativo="Primaria", blogs =[]):
		#Inicializar atributos
		self.nombre = nombre
		self.usuario = usuario
		self.contraseña = contraseña
		self.edad = edad
		self.nivelEducativo=nivelEducativo
		self.blogs = blogs

	def addBlog(self, titulo, fecha, contenido):
		#Creación de objeto tipo Blog
		nuevoBlog = Blog(titulo, fecha, contenido)

		#Chequear si existe blog
		existe = False
		for articulo in self.blogs:
			if articulo.titulo == nuevoBlog.titulo:
				existe = True

		if not existe:
			self.blogs.append(nuevoBlog)

	def cambiarContra(self, contra):
		self.contraseña = contra

	def actualizarNivelEducativo(self, nivel):
		self.nivelEducativo = nivel