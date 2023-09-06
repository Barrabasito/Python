from Figura import Figura
from Color import Color

class Cuadrado(Figura,Color):
    def __init__(self,color,lado):
        Figura.__init__(self,lado,lado)
        color.__init__(self,color)
        
    def CalcularArea(self):
        return self._largo*self._ancho
    
    def __str__(self) -> str:
        return f"{Figura.__str__(self)}{Color.__str__(self)} Area: {self.CalcularArea()}"
    
Cuadrado1=Cuadrado("rojo",5)
print(Cuadrado1)