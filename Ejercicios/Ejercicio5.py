#EJERCICIO 5 PHYTON JOSÉ MARÍA SALAZAR GÓMEZ

frase = input("Introduce una frase: ")
letra_para_reemplazar = input("Introduce la letra que quieras: ")
letra_reemplazo = input("Introduce la letra por la que quieres reemplazarla: ")

Cantidad = frase.count(letra_para_reemplazar)
frase_modificada = frase.replace(letra_para_reemplazar, letra_reemplazo)

print(f"{Cantidad} apariciones.")
print("Resultado:", frase_modificada)
