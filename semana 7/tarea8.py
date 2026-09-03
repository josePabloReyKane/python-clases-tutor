class Libros:
   

    def __init__(self,titulo,autor,edcantidad_paginas,identificacion):
        self.titulo=titulo
        self.autor=autor
        self.edcantidad_paginas=edcantidad_paginas
        self.identificacion=identificacion

    def __str__(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nPaginas: {self.edcantidad_paginas}\nidentificacion: {self.identificacion}"

class Usuario:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

class Presetamo:

    def __init__(self,usuario,libros,plazo):
        self.usuario=usuario
        self.libros=libros
        self.plazo=plazo



class Gestion:

    def __init__(self,libros_T):
        self.libros_T=libros_T

    def agregar(self,libros):
        self.libros_T.append(libros)
        pass

    def buscar(self,identificacio):
        for i in self.libros_T:
            if identificacio==i.identificacion:
                return True
        return False    

    def listar(self):
        for i in self.libros_T:
            print(i)


c=Libros("dracula","bram stoker",350,1)
d=Libros("el hobbit","j.r.r tolkien",450,2)
f=Libros("El Conde de Montecristo ","Alejandro Dumas",650,3)


gestion=Gestion(libros_T=[c,d,f])


e=Libros("harry potter 1","j.k Rowling",550,4)
gestion.agregar(e)

gestion.listar()


print(gestion.buscar(2))