
import random
numero_aleatorio = random.randint(0, 100)


numero=0
cont=0

while numero_aleatorio!=numero:

    numero=int(input("selecione un numero " ))


    if numero_aleatorio>numero:
        print("el numero es mayor al que buscamos ")
        cont=cont+1
        print(f"numero de errores {cont}")
        if cont==10:
            print("perdistes")
            print(f"es el numero correcto {numero_aleatorio}")
            break
        

    if numero_aleatorio<numero:
        print("el numero es menor al que buscamos ")
        cont=cont+1
        print(f"numero de errores {cont}")
        if cont==10:
            print("perdistes")
            print(f"es el numero correcto {numero_aleatorio}")
            break
    if numero_aleatorio==numero:
        print(f"ganastes")

