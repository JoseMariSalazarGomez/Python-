#EJERCICIO PHYTON JOSÉ MARÍA SALAZAR GÓMEZ

pregunta1 = int(input("Indica tu edad: "))
pregunta2 = int(input("Indica tu nomina: "))
pregunta3 = input("Indica tu nombre: ")

if pregunta1 >= 18:
    if pregunta2 < 1000:
        print("Se te aplicará la deduccion")
    else:
        print(f"{pregunta3}, No se te aplicará la deduccion ya que tu salario no corresponde con los requisitos")
        
elif pregunta2 > 1000:
    print(f"{pregunta3}No cumples ninguna condicion")
else:
    print(f"{pregunta3}, usted no cumple la mayoria de edad")