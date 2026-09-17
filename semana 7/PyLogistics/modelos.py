class Vehiculo:
    total_vehiculos = 0

    def __init__(self,carga_maxima_kg):
        self._id_vehiculo = 0
        self.carga_maxima_kg=carga_maxima_kg
        self.carga_actual_kg=0.0

        Vehiculo.total_vehiculos += 1

    def  agregar_carga(self,peso_kg):

        if self.carga_actual_kg+peso_kg>=self.carga_maxima_kg:
            print("el peso supero lo permitido")
        else:
            self.carga_actual_kg=self.carga_actual_kg+peso_kg
    def __str__(self):
        return f"""ID:{self._id_vehiculo}
        Carga actual:{self.carga_actual_kg}
        Carga Permitida:{self.carga_maxima_kg}"""



class Camion(Vehiculo):
    def __init__(self,carga_maxima_kg,numero_ejes):
        super().__init__(carga_maxima_kg)
        self.numero_ejes=numero_ejes
        self.lista_paquetes = []

    def agregar_paquete(self, codigo, peso, destino):
        paquete = {
            "codigo": codigo,
            "peso": peso,
            "destino": destino
        }

        self.lista_paquetes.append(paquete) 

    def __repr__(self):
        return f"""ID:{self._id_vehiculo}
        Carga actual:{self.carga_actual_kg}
        Carga Permitida:{self.carga_maxima_kg}
        Numero de ejes:{self.numero_ejes}
        lista de paquete:{self.lista_paquetes}
        """