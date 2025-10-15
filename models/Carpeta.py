class Carpeta:
    def __init__(self, nombre):
        self._nombre=nombre
        self._referencias_mensajes=[] #lista de objetos referencias a mensajes 
        self._subcarpetas={} #dic de objetos carpeta 

    def agregar_subcarpeta(self, nombre_subcarpeta):

        if nombre_subcarpeta in self._subcarpetas:
            raise ValueError(f"Ya existe una subcarpeta con el nombre '{nombre_subcarpeta}'.")

        nueva_carpeta = Carpeta(nombre=nombre_subcarpeta)
        self._subcarpetas[nombre_subcarpeta] = nueva_carpeta
        print(f"Subcarpeta '{nombre_subcarpeta}' agregada a '{self._nombre}'.")



    def agregar_referencia_mensaje(self, nueva_referencia):
        pass

    def buscar_mensaje(self, criterio):
        pass
