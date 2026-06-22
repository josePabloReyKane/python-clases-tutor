
import random
    
partidas=0
partidasLose=0
partidasWin=0        


def juego1():

    global partidas,partidasLose,partidasWin

    numero_aleatorio = random.randint(0, 100)
   
    intentosPermitidos = 7
    numero=0
    cont=0

    

    while numero_aleatorio!=numero:

        numero=int(input("selecione un numero " ))


        if numero_aleatorio>numero:
            print("el numero es mayor al que buscamos ")
            cont=cont+1
            if cont==intentosPermitidos:
                print("perdistes")
                partidasLose = partidasLose+1
                return partidasLose 
                break
                
        

        if numero_aleatorio<numero:
            print("el numero es menor al que buscamos ")
            cont=cont+1
            if cont==intentosPermitidos:
                print("perdistes")
                partidasLose=partidasLose+1
                return  partidasLose
                break 
                
                
                
        if numero_aleatorio==numero:
            
            print(f"ganastes")
            partidasWin=partidasWin+1
            return partidasWin
            break


def juego2():

    global partidas,partidasLose,partidasWin

    intentosPermitidos = 10
    numero_aleatorio = random.randint(0, 100)
    numero=0
    cont=0
    while numero_aleatorio!=numero:

        numero=int(input("selecione un numero " ))
        if numero<numero_aleatorio:
            print("el numero es mayor al que buscamos ")

            if numero_aleatorio-numero>=25 :
                print("frio")
                cont=cont+1
                print(f"CONTADOR {cont}")
                if cont==intentosPermitidos:                                
                    print("perdistes")
                    print(f"es el numero correcto {numero_aleatorio}")
                    partidasLose=+1
                    break
            if 10<numero_aleatorio-numero<25 :
                print("medio")
                cont=cont+1
                print(f"CONTADOR {cont}")
                if cont==intentosPermitidos:
                    print("perdistes")
                    print(f"es el numero correcto {numero_aleatorio}")
                    partidasLose=+1
                    break
            if 1<=numero_aleatorio-numero<=10:
                print("caliente")
                cont=cont+1
                print(f"CONTADOR {cont}")
                if cont==intentosPermitidos:
                    print("perdistes")
                    print(f"es el numero correcto {numero_aleatorio}")
                    partidasLose=+1
                    break

        if numero>numero_aleatorio:
            print("el numero es menor al que buscamos ")
            if numero-numero_aleatorio>=25 :
                print("frio")
                cont=cont+1
                print(f"CONTADOR {cont}")
                if cont==intentosPermitidos:                                
                    print("perdistes")
                    print(f"es el numero correcto {numero_aleatorio}")
                    partidasLose=+1
                    break
            if 10<numero-numero_aleatorio<25 :
                print("medio")
                cont=cont+1
                print(f"CONTADOR {cont}")
                if cont==intentosPermitidos:
                    print("perdistes")
                    print(f"es el numero correcto {numero_aleatorio}")
                    partidasLose=+1
                    break
            if 1<=numero_aleatorio-numero<=10:
                print("caliente")
                cont=cont+1
                print(f"CONTADOR {cont}")
                if cont==intentosPermitidos:
                    print("perdistes")
                    print(f"es el numero correcto {numero_aleatorio}")
                    partidasLose=+1
                    break        
        if numero_aleatorio==numero:
            partidasWin=+1
            print(f"ganastes")


entrada=0
entrada2=0
while entrada!=3:


    print("Bienvenido a adivina el numero")
    print("1.Entrar a jugar ")
    print("2.Ver estadistica del juego ")
    print("3.Salir del jugar ")
    entrada=int(input("   "))

        

    if entrada==1:
        
        

        
        numero=0
        cont=0
        print("Selecione nivel de dificultad")
        print("1.Facil(10 intentos) ")
        print("2.dificil(7 intentos) ")
        print("3.Regresar al inicio")
        entrada2=int(input("  "))
        while entrada!=4:
            if entrada2==1:
                partidas=+1
                juego2()
                break

            if entrada2==2:
                juego1()
                break


            if entrada2==3:
                print("regresado al incio")
                break

         
    if entrada==2:
        print(f"Partidas jugadas {partidas}")
        print(f"juegos perdidos {partidasLose}")      
        print(f"juegos ganados {partidasWin}")    
    if entrada==3:
        print("saliendo del programa")
        break
        3

