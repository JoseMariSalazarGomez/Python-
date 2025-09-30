#Ejermplo de tipo de datos

nombre = input("Buenos días, introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))  # Convertimos a entero

if edad >= 110:
    print("Tu edad es incorrecta")
else:
    print("Hola " + nombre + ", tu edad es: " + str(edad))