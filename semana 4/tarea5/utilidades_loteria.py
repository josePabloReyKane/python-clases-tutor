import estatistics,archivo,systema,timepo,ganador

def formatear_numero(numero):
#"""Formatea un numero de loteria con ceros a la izquierda"""

    return str(numero).zfill(5)

def validar_numero_loteria(numero):
#"""Valida que un numero este en rango valido (0-99999)"""

    try:
        num = int(numero)
        return 0 <= num <= 99999
    except ValueError:
        return False

def calcular_premio(numero_jugado, numero_ganador, tipo="exacto"):
#"""Calcula el premio segun tipo de acierto"""

    premios = {
    "exacto": 200000000, # 200 millones
    "aproximacion": 50000000, # 50 millones
    "3_cifras": 500000, # 500 mil
    "2_cifras": 100000
    }
# 100 mil
    return premios.get(tipo, 0)

def obtener_terminaciones(numero):
#"""Obtiene las terminaciones de 2, 3 y 4 cifras"""
    num_str = str(numero).zfill(5)
    return {"2_cifras": num_str[-2:],"3_cifras": num_str[-3:],"4_cifras": num_str[-4:]}