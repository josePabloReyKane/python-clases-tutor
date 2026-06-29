
def matricular_curso(lista_curso,cursos_matriculados):
    """lista curso

    Args:
        lista_curso (lista): todos los curso disponibles
        cursos_matriculados (lista): los curso matriculados hasta ahora
    """

    codigo=input("Codigo del curso: ").strip()
    aux=cursos_matriculados.copy()


    for curso in lista_curso:
        c = list(curso.keys())[0]
        if codigo==c:
            aux.append(curso)
            break

    return aux 


def desmatricular_curso(cursos_matriculados):
    codigo=input("Codigo del curso: ").strip()
    aux=[]
    for curso in cursos_matriculados:
        c = list(curso.keys())[0]
        if codigo==c:
            continue
        else:
            aux.append(curso)

    return aux 

def leer_curso_matriculados(cursos_matriculados):
    for curso in cursos_matriculados:
        codigo = list(curso.keys())[0]
        
        print(f"""codigo del curso {codigo}
                
                -------------------------------------
            """)
