#EJERCICIO 4 PHYTON JOSÉ MARÍA SALAZAR GÓMEZ

posicion = int(input("Introduce la posición inicial: "))
longitud = int(input("Introduce la longitud del substring: "))
frase = input("Introduce la frase: ")

substring = frase[posicion:posicion + longitud]

print("Resultado:", substring)