import datetime

class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo, fecha):
        self._remitente=remitente
        self._detinatario=destinatario
        self._asunto=asunto
        self._cuerpo=cuerpo
        self._fecha=datetime.datetime.now()
    
    def getRemitente(self):
        return self._remitente  
    def getDestinatario(self):
        return self._detinatario
    def getAsunto(self):    
        return self._asunto
    def getCuerpo(self):
        return self._cuerpo
    def getFecha(self):
        return self._fecha
   
    
   
    
