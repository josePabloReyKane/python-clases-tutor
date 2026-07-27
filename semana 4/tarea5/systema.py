import sys

# Mostrar version de Python
print(f"Python version: {sys.version}")


# Verificar argumentos de linea de comandos
if len(sys.argv) > 1:
    modo = sys.argv[1]


print(f"Modo: {modo}")
 # Salir del programa con codigo de estado
if error_critico:
    print("Error critico detectado")
    sys.exit(1)