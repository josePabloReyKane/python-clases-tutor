import random

 # Generar numero ganador (00000-99999)
def generador_ramdom():
        
    numero_ganador = random.randint(0, 99999) 


    # Generar serie ganadora (A-Z)
    series = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    serie_ganadora = random.choice(series)

    # Simular venta de billetes aleatorios
    billetes_vendidos = random.sample(range(100000), 1000)


    # Generar multiples ganadores para aproximaciones
    aproximaciones = [numero_ganador- 1, numero_ganador + 1]