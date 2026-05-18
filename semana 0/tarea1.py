

def Restaurante():
    """Como Calular la divicion de la cuenta para un grupo de personas en un restaurante
    nombre  :string()
    asientos : int
    alimeta : float
    propina : float
    porcenta : float
    divicion : float
    
    """

    
    nombre = input("¿Como te llamas ")
    
    mesaje1=f"hola {nombre} Bienvenido a La Taqueria"
    
    print(mesaje1)

    asientos = int(input("¿Por cuantas personas vas  a dividir la cuenta?"))
    
    alimeta=float(input("Monto de cuenta "))
    
    propina=float(input("Que porcentaje de propina desea dejar?(10, 20, 30)"))
    
    porcenta=alimeta*(propina/100)
    
    total=porcenta+alimeta
    
    divicion=total/asientos
    
    mesaje2=f"---Resumen de la Cuenta---\nCuenta original:{alimeta}\n Propina {propina}%: {porcenta} \n Total a pagar:{total}\nCada persona debe pagar:{divicion}\nGracias por elegirnos"
    
    print(mesaje2)
    
    

Restaurante()