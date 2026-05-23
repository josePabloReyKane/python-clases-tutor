# Problema 18: Números primos (básico)
# RETO: Pide un número al usuario
# Conta cuántos divisores tiene entre 1 y el número mismo
# Si tiene solo 2 divisores, es primo. Muestra si es primo o no.
"""
numero =int(input("seleccione un numero: "))
cont=0

for i in range(1,numero+1):
    if numero%i==0:
        
        cont+=1



if cont==2:
    print(f"el {numero} es primo")

else:
    print(f"el {numero} no es primo")
"""

    # Problema 19: Adivina el número (while)
# RETO: Crea un juego de adivinanza:
# - El programa "piensa" en el número 50
# - El usuario tiene intentos ilimitados para adivinarlo
# - Si es mayor, muestra "Muy alto"
# - Si es menor, muestra "Muy bajo"
# - Si adivina, muestra "¡Ganaste!" y el número de intentos

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
    

# Problema 20: Pirámide de números (for)
# RETO: Pide al usuario un número (altura)
# Crea una pirámide de esa altura
# Ejemplo (si ingresa 5):
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
"""
num=int(input("escriba un numero "))

for i in range(1,num+1):

    for j in range(1,i+1):
        print(f"{j}", end=" " )
    print()
"""
# Problema 21: Suma de dígitos
# RETO: Pide al usuario un número positivo
# Suma los dígitos uno a uno
# Ejemplo: Si ingresa 123, suma 1 + 2 + 3 = 6
# Muestra el resultado
"""
string = "1234"
numero=input("escriba un numero ")

suma=0

for letra in numero:
    suma += int(letra)

print(suma)
"""
