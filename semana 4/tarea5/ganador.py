import random

 # Generar numero ganador (00000-99999)

numero_ganador = random.randint(0, 99999)


# Generar serie ganadora (A-Z)
series = ["A", "B", "C", "D", "E"]
serie_ganadora = random.choice(series)

 # Simular venta de billetes aleatorios
billetes_vendidos = random.sample(range(100000), 1000)


 # Generar multiples ganadores para aproximaciones
aproximaciones = [numero_ganador- 1, numero_ganador + 1]