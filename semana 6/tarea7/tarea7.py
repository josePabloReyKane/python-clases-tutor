import csv
import os


Achivo_inventario="invetario.csv"
Encabezado=["codigo","producto", "cantidad", "precio", "categoria"]

def existe():
    if not os.path.exists(Achivo_inventario):
        with open(Achivo_inventario,"w", newline='', encoding='utf-8') as f:
            escritor =csv.writer(f)
            escritor.writerow(Encabezado)    


        

def registra():
 # Permite al usuario ingresar un nuevo producto al CSV.
    print("\n---NUEVO PRODUCTO---")
    codigo=input("codigo del produto: ")
    with open(Achivo_inventario,"r") as f:
        lector=csv.reader(f)
        encabezados=next(lector)

        for fila in lector:
            try:
                if fila[0]==codigo:
                    raise ValueError("codigo no utilizable")
            except ValueError as e:
                print(f"Entrada invalida: {e}")
                return



    producto = input("Nombre del producto: ").strip()
    if not producto:
        print("Error: El nombre no puede estar vacio.")
        return

    try:
        cantidad = int(input("Cantidad disponible: "))
        precio = float(input("Precio unitario: "))
        if cantidad < 0 or precio < 0:
            raise ValueError("Los valores numericos deben ser positivos.")
    except ValueError as e:
        print(f"Entrada invalida: {e}")
        return

    categoria = input("Categoria (Bebida/Comida/Reposteria): ").strip()
    with open(Achivo_inventario, "r") as f:
        contenido = list(csv.reader(f))
        contenido.append([codigo, producto, cantidad, precio, categoria])
    with open(Achivo_inventario, "w", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerows(contenido)

def eliminar():
    resultado=[]

    codigo=input("codigo del produto: ")
    with open(Achivo_inventario,"r") as f:
        lector=csv.reader(f)
        for fila in lector:

            if fila[0]!=codigo:
                resultado.append(fila)
    with open(Achivo_inventario,"w", newline="") as f:
        escritor =csv.writer(f)
        escritor.writerows(resultado)            
   
def actualizar():
    resultado=[]
   
    codigo=input("codigo del produto: ")
    with open(Achivo_inventario,"r") as f:
        lector=csv.reader(f)
        for fila in lector:
            if fila[0]==codigo:
                producto = input("Nombre del producto: ").strip()
                if not producto:
                    print("Error: El nombre no puede estar vacio.")
                    return 
                try:
                    cantidad = int(input("Cantidad disponible: "))
                    precio = float(input("Precio unitario: "))
                    if cantidad < 0 or precio < 0:
                        raise ValueError("Los valores numericos deben ser positivos.")
                except ValueError as e:
                    print(f"Entrada invalida: {e}")
                    return

                categoria = input("Categoria (Bebida/Comida/Reposteria): ").strip()    
                resultado.append([codigo,producto,cantidad,precio,categoria])
            else:
                resultado.append(fila)
    with open(Achivo_inventario,"w") as f:
        escritor =csv.writer(f)
        escritor.writerows(resultado)    

def mostrar():
    with open(Achivo_inventario,"r")as f:
        lector=csv.DictReader(f)
        print("lista de inventario")
        for i,menu in enumerate(lector,1):
            print(f"{i}. {menu["codigo"],menu["producto"],menu["cantidad"] , menu["precio"],menu["categoria"]},")

def menu(): 
    existe()

    while True:
        print("Sistema de Inventario de Cafetería (Café-Stock)")
        print("1.Nuevo producto")
        print("2.Mostrar lista de productos")
        print("3.Eliminar ")
        print("4.Actulizar")
        print("5.Salir")
        opcion=input("Selecione una opcion: ").strip()
        if opcion=="1":
            registra()
        elif opcion=="2":
            mostrar()
        elif opcion=="3":
            eliminar()
        elif opcion=="4":
            actualizar()   
        elif opcion=="5":
            print("Salindo del sistema......")
            break
        else:
            print("Opcion invalida, intente de nuevo.")

menu()