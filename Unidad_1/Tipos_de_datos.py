x = 1 #Enteros
y = 2.2 #Flotantes
z =2 + 3j #Complejos

Xflotante = float(x)
ycomplejo = complex(y)
zentero = int(z)

print(type(x),type(y),type(z))
print(id(x),id(y),id(z))
print(Xflotante,ycomplejo,zentero)

#booleanos
x=True
if x:
    print('x')
    
y=False
if not y:
    print('y')
    x=[]#
    x={}
    x={0}#Set
    
#Cadenas
x="Hola Mundo"
print(x)
#Interpolacion sirve para meter variables a las cadenas
saludo = f'saludo:{x}'
print(saludo)
#Concatenacion
saludo='Saludo: '+x+',Despedida:'+str(y)
print(saludo)
#""Para texto multilineas
texto="""
Hola
"""
#Interpolacion
texto=f"""
Hola
"""

print(x,y,z,sep=-,end=/)

#FORMAS DE REVERTIR CADENAS
nombre="Luis Daniel Castillo"


print(nombre[::-1])
#COLOCAR INDICES
print(nombre[-1])
print(''.join)