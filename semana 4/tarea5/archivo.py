import os



# Verificar si existe carpeta de datos
if not os.path.exists("datos_loteria"):
    os.makedirs("datos_loteria")



print("Carpeta de datos creada")
 # Listar archivos de sorteos anteriores
archivos = os.listdir("datos_loteria")

print(f"Sorteos guardados: {len(archivos)}")

# Obtener informacion del sistema
print(f"Sistema operativo: {os.name}")
print(f"Directorio actual: {os.getcwd()}")

