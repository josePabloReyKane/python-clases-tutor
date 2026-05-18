
def examenes(nota1: float ,nota2: float,nota3: float):
"""
Notas de los examenes realizados
    nota1: float 
    nota2: float 
    nota3: float 
    
    resultado :float
"""
    resultado=(nota1/100)*10+(nota2/100)*10+(nota3/100)*10

    return resultado

def proyectos(pro1: float, pro2: float):
""" 
    resultado de los proyectos propuestos en clases
    pro1 : float
    pro2 : float
"""

    resul=(pro1/100)*15+(pro2/100)*15
    
    
    return resul

def tareas(num : int):
    
    """numero de tareas entregas son del 1 al 10
        num :int
    
    """
    
    entregadas=(numero/10)*20
    
    return entregadas

nombre=input("Nombre del estudiante")
curso=input("Nombre del curso")

num1=float(input("nota de examen 1"))
num2=float(input("nota de examen 2"))
num3=float(input("nota de examen 3"))
num4=float(input("nota de proyecto 1"))
num5=float(input("nota de proyecto 2"))
num6=float(input("tareas entregadas(1 al 10)"))
num7=float(input("escriba del valor de participacion( 1 al 10 )"))
final=examenes(num1,num2,num3)+proyectos(num4,num5)+tareas(num6)+num7

if final<65:
    estado="----REPROBADO----"
if final>=65 or final<=69:
    estado="----Convocatoria----"
if final>70:
    
    estado="----Aprobado----"
if final>90:
    estado="----Aprobado con excelencia----"
    
    
print("----------------------------")
print( "REPORTE DE CALIFICACIONES")
print("----------------------------")
print("Estudiante: {nombre}")
print("Curso: {curso}")
print("--Desglose de notas--")
print("Examenes (40%): {examenes}")
print("Proyetos (30%): {proyetos}")
print("Tareas (20%): {tareas}")
print("Participacion (10%): {num7}")
print("---Resultado Final---")
print("Nota Final: {final}")
print("Estado: {estado}")