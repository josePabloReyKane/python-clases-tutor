edad=0
precio=0
platea=0
placo=0
galeria=0
asiento=0
asiento_plate=0
asiento_Palco=0
asiento_galeria=0



def venta():

    global precio,platea,placo,galeria,asiento,asiento_Palco,asiento_galeria,asiento_plate
    opcion2=0
    
       
    while(opcion2!=4):
        print("1.Comprar boleto en platea")
        print("2.Comprar boleto en palco")
        print("3.Comprar  boleto en galeria")
        print("4.Salir")
        opcion2 =int(input("selecione una opcion: " ))

        match opcion2:
            case 1:
                numero=int(input("numeros de asientos que deseas comprar: "))
                asiento_plate=asiento_plate+numero
                if(asiento<=12):
                    platea=2500*asiento_plate
                else:
                    asiento_plate=asiento_plate-numero 
                    asiento=asiento-numero
                    print(f"""Solo puedes comprar 12 asiento 
                          tienes actualmente {asiento}""")                  
                print("gracias por comprar")
     
            case 2:
                numero=int(input("numeros de asientos que deseas comprar: "))
                asiento_Palco=asiento_Palco+numero
                asiento=asiento+numero
                if(asiento<=12):
                    placo=1500*asiento_Palco
                else:
                    asieasiento_Palconto=asiento_Palco-numero 
                    asiento=asiento-numero
                    print(f"""Solo puedes comprar 12 asientotienes actualmente {asiento}""")    
                print("gracias por comprar")
                

            case 3:
                numero=int(input("numeros de asientos que deseas comprar: "))
                asiento=asiento+numero
                asiento_galeria=asiento_galeria+numero
                if(asiento<=12):
                    placo=8000*asiento_galeria
                else:
                    asiento_galeria=asiento_galeria-numero
                    asiento=asiento-numero
                    print(f"""Solo puedes comprar 12 asiento tienes actualmente {asiento}""") 
                print("gracias por comprar")
                

            case 4:
                print("saliendo")
                break
            case _:
                print(("opcion invalida"))
                continue
        
def limpiar():
    platea=0
    placo=0
    galeria=0
    asiento=0
    asiento_plate=0
    asiento_Palco=0
    asiento_galeria=0

def factura():
    descuento=0
    
    if(edad>=65):
        descuento=total*0.3
        total=platea+placo+galeria-descuento
    else:
        total=platea+placo+galeria
        

    print(f"""  
        FACTURAL DE BOLETERIA
        Boletos comprardos por asiento
        Platea: {asiento_plate}
        Palco: {asiento_Palco}
        Galeria: {asiento_galeria}
        Total: {asiento}

        Costo de boletos
        Platea: {platea}
        Palco: {placo}
        Galeria: {galeria}
        descuento: {descuento}
        Total: {total}

     """)


    



def main():
    global edad
    total=0

    

    print("Nombre del Usuario: ")
    nombre=input("")
    print("Edad del Usuario: ")
    edad=int(input(""))
    if(edad>=18):
        while True:
        

            try:

                print("1.Comprar boleto")
                print("2.Eliminar boleto")
                print("3.Salir")
                opcion =int(input("selecione una opcion: " ))
                
                match opcion:
                    case 1:
                        venta()
                    case 2:
                        limpiar()
                        print("boletos eliminados")
                    case 3:
                        factura()
                        if(edad>=65):
                            total=(placo+placo+galeria)*0.7
                            print(f"costo total {total}")

                        else:
                            total=placo+placo+galeria
                            print()
                            print(f"costo total {total}")
                                
                        print("saliendo")
                        break
                    case _:
                        ValueError
                        continue
            except ValueError:
                print(("opcion invalida"))
    else:
        print("no puedes realizar la compra")

   



main()