import statistics

# Lista de precios de billetes vendidos

precios = [10000, 10000, 10000, 5000, 5000]

 # Calcular estadisticas de ventas





promedio_precio = statistics.mean(precios)
mediana_precio = statistics.median(precios)
moda_precio = statistics.mode(precios)
 # Calcular desviacion estandar de numeros jugados
numeros_jugados = [12345, 54321, 98765, 11111]

desv_std = statistics.stdev(numeros_jugados)