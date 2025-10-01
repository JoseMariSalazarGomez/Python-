#EJERCICIO 3 PHYTON JOSÉ MARÍA SALAZAR GÓMEZ

frase = input("Introduzca una frase: ")

long = len(frase)

frase1 = frase[:3]
frase2 = frase[long-3:]

print(f"La frase compuesta es: {frase1}{frase2}")