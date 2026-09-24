import csv 
import os 
from modelos import Vehiculo, Camion
    


def registrar_evento_bitacora(mensaje: str, ruta_txt: str = "bitacora.txt") -> None:
    # 1. Abrir el archivo ruta_txt
    # 2. Agregar (append) el mensaje en el archivo
    # Esta función va a ser llamada a lo largo del programa dependiendo del nivel
    # de detalles que queremos en la bitácora
    archivo= open(ruta_txt,"a")
    archivo.write(mensaje) 
    archivo.close()  
    


def exportar_paquetes_csv(flota: dict, ruta_csv: str = "reporte_paquetes.csv") -> None:
    # 1. Abrir el archivo ruta_csv
    # 2. Crear objeto writer (csv.writer(archivo_csv)) 
    # 3. Creas los encabezados (encabezados = ["ID_Vehiculo", "Codigo_Paquete", "Peso_KG", "Destino"])
    # 4. Escribimos los encabezados primero (writer.writerow(encabezados))
    # 5. Iteramos los camiones de la flota
    # 6. Por cada paquete de cada lista de paquetes de los camiones, voy a ir escribiendo las filas
    # 6.1 fila = [id_vehiculo, codigo_paquete, peso_paquete, destino_paquete]
    # 6.2 writer.writerow(fila)
    Achivo_inventario="Camiones.csv"
    Encabezado=["ID_Vehiculo", "Codigo_Paquete", "Peso_KG", "Destino"]
    if not os.path.exists(Achivo_inventario):
            with open(Achivo_inventario,"w", newline='', encoding='utf-8') as f:
                escritor =csv.writer(f)
                escritor.writerow(Encabezado)



    ... 

def leer_bitacora(ruta_txt: str = "bitacora.txt") -> None:
    # 1. Chequear si existe la ruta con os.path.exists
    # 2. Abrir el archivo en la ruta (open(ruta_txt, mode="r"))
    # 3. Leerlo (archivo.read() o archivo.readlines())

    archivo=open(ruta_txt,"r")
    if archivo != False:
        print(archivo.read())

    archivo.close()