nombre = "paco"
clave = "hola123"
pregunta1 = input("Introduce tu nombre: ")
if pregunta1 == nombre:
    pregunta2 = input("Introduce tu clave: ")
    if pregunta2 == clave:
        print("Bienvenido al sistema")
    else:
        print("Clave Incorrecta")
else:
    print("Nombre incorrecto")