import utilidades_loteria

numero = utilidades_loteria.formatear_numero(1234)

 # O importar funciones especificas
from utilidades_loteria import validar_numero_loteria, calcular_premio

if validar_numero_loteria(numero_jugado):
    premio = calcular_premio(numero_jugado, ganador, "exacto")