def suma():
    return 10 + 5
print(suma())

def suma(a:int,b:int)->int:
    return a + b
print(suma(10,15))

x=10
z=50
y=2
def multiplicacion(a,b,c):
    return a*b*c
print(multiplicacion(x,z,y))
#Python tiene la funcionalidad de poner un valor si es que no se manad el argumento podemos ponerlo de esta forma

def multiplicacion(a,b,c=1):
    return a*b*c
print(multiplicacion(x,z))

# la funcion help() es una funcion de python que te ayuda saber que es 

lista=[1,2,3,4]
def suma(x):
    for i in x:
        suma+=i
        return suma
print(suma(lista))

#Si yo pongo asi quiero decir que va recibir una tupla de valores o parametros recibe n parametros
def suma(*x):
    print(type(x))
    suma=0
    for i in x:
        suma+=i
    return suma
print(suma((1,2,3,4,5,6,7,8,32,1,2)))

#Al moento que se pasen se convierten en una tupla los parametros que vamos a mandar seguidos de un coma
def restar(*numeros):
    resta=0
    for i in numeros:
    resta-=i
    return resta
print(restar(1,2,3,4,5,6,7,8,2,1))

#cuando colocamos doble * esto quiere decirque va ser valores con llave y se convierte en diccionario

def sumar(**kwargs):
    suma=0
    print(kwargs)
    print(type(kwargs))
    for Key




print(sumar(a=10,b=5,c=25,d=62))

di={'a':10,'b':11,'c':12,'d':9}
sumar(**di)

#return una sentencia que devuelve
def miFuncion():
    print("Entra")
    return
    print("sale")
#Puede devolver mas de un valor
def SumarMedia(*x):
    suma=0
    for n in x:
        suma+=n
    media=suma/len(x)
    return suma,media
resultado=SumarMedia(1,2,3,4,5,3,2)
print(resultado)


#Una funcion puede tomar diversos valores
def function(a,b,*args,**kwargs):
    print('a',a)
    print('b',b)
    for arg in args:
        print('arg ',arg)
    for key,value in kwars.items():
        print(key,'=',value)
function(1,6,'k',4,2,4,"Hola",e=1,e=4,e=10)



numeros = list(range(1,101,1))
def suma(*numeros):
    suma=0
    for n in numeros:
        suma+=n
    return suma
print(suma(*numeros))

lambda *n:print((sum(n)))(*list(range(1,101,1)))



def multiplicador(n):
    return lambda a:print(a*n)
duplicador=multiplicador(2)
triplicador=multiplicador(3)
print(duplicador(11))
print(triplicador(11))


#try except
try:
    suma=1+"1"
except Exception as e:
    print(e)
else:
    print("Else suma ",suma)
finally:
    print("Finally",suma)

