#cualquier clase que crees hereda de object
#self esel this en c#
#__init__ es el constructor
class rectangulo:
    def __init__(self):
        self._ancho=ancho
        self._largo=largo
        
    @property
    def Ancho(self):
        return self._ancho
    @Ancho.setter
    def Ancho(self,ancho):
        self._ancho=ancho
        
    def CalcularArea(self):
        return self._ancho*self._largo
    def CalcularPerimetro(self):
        return(self._ancho*2)+(self._largo*2)
    
class Cuadrado: