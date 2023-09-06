#Diccionario es parecido a JSON utilizan llave valor, 
# la propiedad que hace referencia a lo que guarda no son ordenadas son indexadas, el indice es la llave en questionson mutables.
dic={
    "Nombre":"Rocio",
    "Edad":24,
    "Promedio":10.0
    }
print(dic("Promedio"))
#Se pueden declarar con el constructor
#dic= dic({})

#Para modificar
dic["Nacionalidad"]="Mexicana"
dic["Edad"]=25
print(dic)

#Como se itera es diferente ya que tenemos la llave y el valor
for d in dic:
    print(d)

for d in dic:
    print(dic[d])

for k,v in dic.items():
    print(k,v)

print(dic.items())
li=list(dic.items())
print(li)

#Si hacemos referencia a una llave que no existe nos marcara error
print(dic["Nombre"])
print(dic.get("Nombre","No existe nombre"))
print(list(dic.keys()))
print(list(dic.values()))
print(dic.popitem())



    
