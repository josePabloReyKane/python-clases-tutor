import statistics
import os 
import sys 

from modelos import Vehiculo, Camion

import random 


estados_entrega = ("EN_ALMACEN", "EN_TRANSITO", "ENTREGADO")

def inspeccion_seguridad(id_vehiculo: str) -> bool:
    print("Iniciando inspeccion de seguridad")

    # Simular 5 pasos
    # bucle for que funciona 5 veces 

    fallo_alguna_vez = False

    for i in range(0, 5):
        # Hay un solo True porque se ocupa una probabilidad 
        # de 20% de fallo
        print(f"Revisando punto #{i}")
        
        fallo = random.choice([True, False, False, False, False])

        if fallo == True:
            print(f"La inspección falló en el número {i}")
            fallo_alguna_vez = True
            break
        else:
            print(f"Pasó punto {i}")

    if fallo_alguna_vez == True:
        return False
    else:
        return True


def calcular_promedio_peso_paquetes(flota: dict) -> float:
    """ 
    flota = {
        "1": Camion(),
        "2": Camion(),
        "3": Camion()
    }

    # Esto accede a la lista de paquetes
    print(flota["1"].lista_paquetes)

    n = Vehiculo.total_vehiculos # cantidad de vehiculos en la flota

    # Iterar los valores de un diccionarios
    for camion in flota.values():
        # ahora camion se va a 
        # utilizar como una instacia

        for paquete in camion.lista_paquetes:
            paquete["peso"]

    for paquete in flota["1"].lista_paquetes:
        # yo se que paquete se va a ver así:
        # paquete = {
        #     "codigo": 1289,
        #     "peso": 17000,
        #     "destino": mcdonalds
        # }
        print(paquete["peso"])
    """
    ...


def verificar_directorio(ruta_directorio: str) -> None:
    """ 
    os.path.exists(ruta_directorio) => devuelve True o False dependiendo si existe el directorio
    os.makedirs(ruta_directorio) => Crea un directorio en la ruta

    """

    # Si no existe un directorio, lo crea
    ...
