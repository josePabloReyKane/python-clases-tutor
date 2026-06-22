


def agregar_curso(lista_curso):
    aux=lista_curso.copy()
    codigo=input("Codigo del curso").strip()
    profe=input("nombre del profesor")
    curso={codigo:profe}
    aux.append(curso)
    return aux




def leer_curso(lista_curso):
    for curso in lista_curso:
        codigo = curso.keys()[0]
        profesor = curso[codigo]
        print(f"""codigo del curso {codigo}
                nombre profesor {profesor}
                -------------------------------------
            """)


def actualizar_curso(lista_curso):
    codigo=input("Codigo del curso").strip()
    aux=[]

    for curso in lista_curso:
        c=curso.keys()[0]
        if codigo==c:
            codigo=input("Codigo del curso").strip()
            profe=input("nombre del profesor")
            curso={codigo:profe}
            aux.append(curso)
        else:
            aux.append(curso)

    return aux 
    

def eliminar_curso(lista_curso):
    codigo=input("Codigo del curso").strip()
    aux=[]

    for curso in lista_curso:
        c=curso.keys()[0]
        if codigo==c:
            continue
        else:
            aux.append(curso)

    return aux  