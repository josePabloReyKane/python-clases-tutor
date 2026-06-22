def login():
    usuario=input("nombre usuario: ")
    contrasena=input("contraseña: ")

    if usuario=="admin" and contrasena=="admin123":
        print("bienvenido admin")



    elif usuario=="estudiante" and contrasena=="u123":
        print("bienvenido estudiante")

    else:    
        print("usuario incorrecto")

    return usuario




