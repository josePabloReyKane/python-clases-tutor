import csv
import os
Achivo_inventario="invetario.csv"
Encabezado=["producto", "cantidad", "precio", "categoria"]

def existe():
    if not os.path.exists(Achivo_inventario):
        with open(Achivo_inventario,"w", newline='', encoding='utf-8') as f:
            escritor =csv.writer(f,fieldnames=Achivo_inventario)
            escritor.writerows()    


        

def registra():
 # Permite al usuario ingresar un nuevo producto al CSV.
    print("\n---NUEVO PRODUCTO---")
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
    with open("inventario.csv","a",newline="")as f:
        escritor =csv.writer(f)
        escritor.writerows(["producto","cantidad","precio","categoria"])

   
def actualizar(producto):
    pass

def mostrar():
    with open(Achivo_inventario,"r")as f:
        lector=csv.DictReader(f)
        print("lista de inventario")
        for i,menu in enumerate(lector,1):
            print(f"{i}. {menu["producto"],menu["cantidad"] , menu["precio"],menu["categoria"]},")

def menu(): 
    existe()

    while True:
        print("Sistema de Inventario de Cafetería (Café-Stock)")
        print("1.Nuevo producto")
        print("2.Mostrar lista de productos")
        print("3.Actualizar ")
        print("4.Salir")
        opcion=input("Selecione una opcion: ").strip()
        if opcion=="1":
            registra()
        elif opcion=="2":
            mostrar()
        elif opcion=="3":
            pass
        elif opcion=="4":
            print("Salindo del sistema......")
            break
        else:
            print("Opcion invalida, intente de nuevo.")

menu()