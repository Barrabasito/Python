from Persona import Persona

class Empleado(Persona):
    def __int__(self,nombre,edad,sueldo)->None:
        super().__int__(nombre,edad)
        self.sueldo=sueldo
    
    def __str__(self)->str:
        return f"{super().__str__()} Sueldo{self._sueldo}"
    
miEmpleado=Empleado("Pedro",25,500)
print(miEmpleado)