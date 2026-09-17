import utilidades
from modelos import Vehiculo, Camion 
from persistencia import registrar_evento_bitacora, exportar_paquetes_csv, leer_bitacora

menu = """
1. Registrar nuevo Camion en la Flota
2. Cargar paquete a un camion
3. Ver estado de la Flota
4. Realizar inspeccion
5. Ver estadísticas y promedio de peso
6. Exportar paquetes a CSV y ver Bitacora
7. Salir
"""

def main():
    flota = {} # Lleva el control de la flota
    print(menu)
    opcion = input("Seleccione una opcion del 1-7").strip()

    match opcion:
        case "1":
            ...
        case "2":
            ...
        case "3":
            ...
        case "4":
            ...
        case "5":
            ...
        case "6":
            ...
        case "7":
            ...
        case _:
            ...