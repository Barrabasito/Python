#La tuplas osn colecciones ordenadas e inmutables y permite datos duplicados
#Una tupla es una coleccion de informcion se denomina porque esta dentro de los parentesis
tupla=(1,2,3)
print(tupla)
print(type(tupla))
#Esto es una tupla de tuplas
tupla=1,2,('a','b'),3
print(tupla)

#Indices en las tuplas
print(tupla[2][0])
tupla=1,2,3

#Agregar elementos
tupla=(1,2,3)
lista=list(tupla)
lista.append(4)
tupla=tuple(lista)
print(tupla)
#Se pueden convertir entre colecciones menos el diccionario

#Ciclo para recorrer
for t in tupla:
    print(t)
    
#Destructuracion
x,y,z,a=tupla
print(x,y,z,a)

#Para poder poner un elemento en una tupla se debe poner , al final
tupla(2,)

#traer el indice si no encunetra l indice truena en pyton a cambio de otro lenguajes que te traen -1
tupla(2,2,2,1,2,4,6)
print(tupla.count(2))#contar los elemento iguales
print(tupla.index(0))

#listas ordenadas, mutable, prmite duplicado
lista=[1,2,3,4]
print(lista)
lista2=list("4567")
print(lista2)
lista3=[1,"2",["12",23,2]]
print(lista3[2][0])

print(lista3[-1])
lista3[2]=10#se puede porque son mutables
print(lista3)
lista4=[1,2,3,4,5,6,7]
print(lista4[0:2])
print(lista4[2:6])
lista4[0:3]=[0,0,0]
print(lista4)
#Operaciones entre listas
lista3+=lista4
print(lista3)

#Iterar
for l in lista3:
    print(l)

for index,l in enumerate(lista3):
    print(index,l)

lista1 = (1,2,3)
lista2=["A","b","C"]
for l1,l2 in zip(lista1,lista2):
    print(l1,l2)
    
for i in range(0, len(lista3)):
    print(lista3[i])

#Concatenar dos listas en una
lista3.append(4)
#Insert el indice y el nuevo elemento y recorrer los demas
lista3.extend([2,1])
#l pop elimina el ultimo por defecto pero podemos indicar que elimine uno en especifico
lista3.pop(1)
#El reverse para invertir la lista
lista3.reverse()

lista3.sort()
lista3.sort(reverse=True)

#Set es una coleccion inmutable y mutable a la vez no deja remover un elemento especifico y poner otro pero agregar e iliminar si deja
set={1,2,3,4,5,6}
print(set)
set.add(9)
print(set)

set2=set{[2,3,4,5,2,1]}
print(set2)
lista=["a","b"]
set=set([lista])#No se puede convertir a set ya que son elementos de la lista mutable sy no concuerdan 

#Se utilizan mucho los set en pyton porque se utilizan mucho en la teoria de conjunto

for s in set2:
    print(s)

s1={1,3,4}
s2={3,5,6}
print(s1^s2)

s1.add(1)
s1.remove(3)#remueve ese elemento en el set

s1.discard(7)#descarta el elemento aunque no este asi no genera error
s1.pop()
s1.clear()
s1.union()
s1.intersection()


