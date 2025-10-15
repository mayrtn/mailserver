from models.CasillaCorreo import CasillaCorreo
class Usuario:
    def __init__(self, email, password):

        self._email=email #el email funciona como ID
        self._password=password
        self._casilla_correo=CasillaCorreo()

    def getEmail(self):
        return self._email
    def getCasillaCorreo(self):
        return self._casilla_correo
    
    
    
