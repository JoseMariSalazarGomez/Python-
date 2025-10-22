num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

while (num1 < num2):
    cantidad = num2 - num1 - 1
    print(f"Hay {cantidad} números entre {num1} y {num2}.")
    break
else:
    print("El primer número debe ser menor que el segundo.")