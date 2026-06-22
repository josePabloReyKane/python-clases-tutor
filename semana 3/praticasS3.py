def saludo(edad):
    """confirmacion de mayoria de edad

    Args:
        edad (int): edad de la persona

    Returns:
        bool: _description_
    """
    if edad >=18:
        return True
    else:
        return False

"""
PROGRAMA DE CALCULADORA

Elabore un programa que tenga las siguientes funciones:
1. Tome la suma de dos números
2. Tome la resta de dos números
3. Tome la multiplicación de dos números
4. Tome la división de dos números
5. Eleve un número a a la potencia b (a ** b)

Implementar un menú para que el usuario elija sus opciones
"""
def suma(a,b):
    """suma de dos numeros enteros

    Args:
        a (float): valor del primer numero
        b (float): valor del segundo numero

    Returns:
        float: resultado de la suma de a+b
    """

    return a+b

def resta(a,b):
    """resta de dos numemros

    Args:
        a (float): valor del primer numero
        b (float): valor del segundo numero

    Returns:
        float: resultado de la resta de a-b
    """

    return a-b

def multiplicacion(a,b):
    """multiplicacion de dos numeros

    Args:
        a (float): valor del primer numero
        b (float): valor del segundo numero

    Returns:
        float: resultado de la multiplicacion  de a*b
    """
    return a*b

def division(a,b):
    """division de dos numeros

    Args:
        a (float): valor del primer numero
        b (float): valor del segundo numero

    Returns:
        float: resultado de la division  de a/b
    """
    return a/b

def potencia(a,b):
    """potencia de numeros

    Args:
        a (int): valor del primer numero
        b (int): valor del segundo numero

    Returns:
        int: resultado de la potencia  de a**b
    """
    return a**b


num1=int(input("elige el primer valor: "))
num2=int(input("elige el segundo valor: "))

print(f"resultados sumar {suma(num1,num2)}")
print(f"resultados resta {resta(num1,num2)}")
print(f"resultados multiplicacion {multiplicacion(num1,num2)}")
print(f"resultados division {division(num1,num2)}")
print(f"resultados potencia+ {potencia(num1,num2)}")
