from datetime import datetime, timedelta

 # Obtener fecha y hora actual
def fecha():
    fecha_actual = datetime.now()
    print(f"Sorteo realizado: {fecha_actual.strftime("%d/%m/%Y %H:%M:%S")}")

    # Calcular proxima fecha de sorteo (cada domingo)

    dias_hasta_domingo = (6- fecha_actual.weekday()) % 7
    proxima_fecha = fecha_actual + timedelta(days=dias_hasta_domingo)
    # Registrar tiempo de sorteo
    inicio = datetime.now()
    # ... realizar sorteo ...
    fin = datetime.now()
    duracion = (fin- inicio).total_seconds()
    print(f"Sorteo completo en {duracion} segundos")
