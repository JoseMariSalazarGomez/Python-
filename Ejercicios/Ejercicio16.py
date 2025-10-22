attempts: 3

while (attempts > 0):
    answer1 = input("Introduzca su nombre: ")
    answer2 = input("Introduzca su contraseña: ")

    if answer1 == "Admin" and answer2 == "123":     
        print("Bienvenido")
        attempts = 3
        break
    else:
        print(f"Has fallado tienes {attempts} intentos") 
        attempts = attempts - 1 
else:
    print("Te has quedado sin intentos")
