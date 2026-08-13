import utilidades_loteria



def menu():
    opcion=0

    while opcion !=8:

        opcion=int(input())
        print("1.Comprar billetes")
        print("2.Realizar sorteo")
        print("3.Ver mis billetes")
        print("4.Resultado ultimo sorteo")
        print("5.Estadisticas")
        print("6.Verificar premios")
        print("7.Informacion del sistema")
        print("8.Salir")
        print("")
        print("-----------------------------------------------")

        opcion=int(input("Elige una opcion: "))
        match opcion:

            case 1:
                print("Lunes")
            case 2:
               print("Lunes")
            case 3:
                print("Lunes")
            case 4:
                print("Lunes")
            case 5:
                print("Lunes")
            case 6:  # varios valores en un mismo caso
                print("Lunes")
            case 7:
                print("Lunes")
            case 8:
                print("saliendo")
            case _:  # caso por defecto (default)
                return "Día inválido"




menu()
    