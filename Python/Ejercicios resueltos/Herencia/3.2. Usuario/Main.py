from Usuario import Usuario


#DESARROLLO INTERACTIVO
#Creación de usuario
user = Usuario(input("Escribe tu nombre: "), int(input("Escribe tu edad: ")), input("Nombre de usuario: "))
print("Definición de contraseña")
while True:
  contra = input("Contraseña: ")
  repite = input("Repite contraseña: ")

  if contra == repite:
    break
  
print("Usuario creado")