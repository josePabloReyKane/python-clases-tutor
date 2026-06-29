import admin
import auth
import usuario

#esa lista de curso disponibles
lista_curso=[]
#esa lista de curso matriculados
lista_curso_matriculados=[]




def main():



    global lista_curso,lista_curso_matriculados
    

    while True:
        nombre_usuario=auth.login()
        opcion=0

        if nombre_usuario=="admin":
            while opcion!=5:

                print("1.AGREGAR")
                print("2.ACTUALIZAR")
                print("3.ELIMINAR")
                print("4.MOSTRAR")
                print("5.SALIR")
                opcion=int(input())



                match opcion:
                    
                    case 1:
                        lista_curso=admin.agregar_curso(lista_curso)

                    case 2:
                        lista_curso=admin.actualizar_curso(lista_curso)

                    case 3:
                        lista_curso=admin.eliminar_curso(lista_curso)

                    case 4:
                        admin.leer_curso(lista_curso)

                    case 5:
                        print("saliendo")
                        break

                    case _:
                        print("OPCION INVALIDA")
        if nombre_usuario=="estudiante":
            while opcion!=5:

                print("1.matricular")
                print("2.desmatricular")
                print("3.ver cursos matriculasdos")
                print("4.ver cursos disponibles")
                print("5.salir")

                opcion=int(input())



                match opcion:
                    
                    case 1:
                        lista_curso_matriculados=usuario.matricular_curso(lista_curso,lista_curso_matriculados)

                    case 2:
                        lista_curso_matriculados=usuario.desmatricular_curso(lista_curso_matriculados)

                    case 3:
                        usuario.leer_curso_matriculados(lista_curso_matriculados)
                    case 4:
                        admin.leer_curso(lista_curso)

                    case 5:
                        print("saliendo")
                        break

                    case _:
                        print("OPCION INVALIDA")

main()

    