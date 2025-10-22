num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

totalpar= 0
totalimpar = 0
contador = num1

while (contador < num2):
    if(contador%2 == 0):
        totalpar = contador + totalpar
    else:
        totalimpar = contador + totalimpar
    
    contador = contador + 1
else:
    print(f"El sumatorio de {num1} y {num2} pares es: {totalpar} e impares es {totalimpar}")
