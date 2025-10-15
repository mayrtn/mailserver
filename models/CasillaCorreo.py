import Carpeta

class CasillaCorreo:
    _CARPETAS_DE_SISTEMA = ['Recibidos', 'Enviados', 'Papelera', 'Spam', 'Borradores']
    
    def __init__(self):
        self._carpetas={}

        for carpeta in self._CARPETAS_DE_SISTEMA:
            nueva_carpeta = Carpeta(carpeta)
            self._carpetas[carpeta] = nueva_carpeta
  
    def getCarpetas(self):
        return list(self._carpetas.keys()) #devuelve una lista con los nombres de las carpetas