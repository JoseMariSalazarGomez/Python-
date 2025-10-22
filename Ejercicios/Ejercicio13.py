adivina = 5
intentos = 0

while(intentos <=3):
    numeroadivina = int(input("Introduce número del 1 al 10: "))

    if (numeroadivina == adivina)
        print(f"Has adivinado el número!!!")
        break
    elif (numeroadivina<adivina):
        print("El numero es menor")
        intentos = intentos + 1
    else:
        print(f"El número es mayor")
        intentos = intentos + 1
else:
    print("Has superado el número de intentos")