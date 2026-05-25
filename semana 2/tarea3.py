
import random
    
partidas=0
partidasLose=0
partidasWin=0        
entrada=0
entrada2=0

def juego1():

    numero_aleatorio = random.randint(0, 100)
   
    intentosPermitidos = 10
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
        print("2.Medio(15 intentos) ")
        print("3.Dificil(9 intentos)")
        print("4.Regresar al inicio")
        entrada2=int(input("  "))
        while entrada!=4:
            if entrada2==1:
                partidas=+1
                juego1()
                break

            if entrada2==2:

                intentosPermitidos = 15
                numero_aleatorio = random.randint(0, 100)
                numero=0
                while numero_aleatorio!=numero:

                    numero=int(input("selecione un numero " ))



                    cont=cont+1
                    if numero_aleatorio-numero>=25 or numero-numero_aleatorio>=25:
                        print("frio")
                        if cont==intentosPermitidos:                                
                            print("perdistes")
                            print(f"es el numero correcto {numero_aleatorio}")
                            partidasLose=+1
                            break
                    if 10<numero_aleatorio-numero<25 or 10<numero-numero_aleatorio<25:
                        print("medio")
                        if cont==intentosPermitidos:
                            print("perdistes")
                            print(f"es el numero correcto {numero_aleatorio}")
                            partidasLose=+1
                            break
                    if 10<numero_aleatorio-numero or  10<numero-numero_aleatorio:
                        print("caliente")
                        if cont==intentosPermitidos:
                            print("perdistes")
                            print(f"es el numero correcto {numero_aleatorio}")
                            partidasLose=+1
                            break
     
                    if numero_aleatorio==numero:
                        partidasWin=+1
                        print(f"ganastes")

            if entrada2==3:
                print("en desarrolo")
                break


            if entrada2==4:
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

