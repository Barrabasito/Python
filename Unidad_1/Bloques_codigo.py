#If y Else
a=5

if a==5:
    print(a)
else:
    print(5)
#If anidado
if a==5:
    print(5)
elif a==6:
    print(5)

#If en linea
x=10
if x==10:print(x):print(x+10)

print("Es 5" if x==5 else "no es 5")

#FOR maneja iteraciones en base los valores que les den
cadena="Hola"
for c in cadena:
    print(c)
#Rangos
for i in range(0,100,2):
    print(i)

#For anidados
tupla=((0,1),(2,3),(4,5))
for i in tupla:
    for j in i:
        print(j)
        
for x in range(0,100):
    pass
#El pass sirve para ignorar codigo

#El cotinue sirve para pasar la siguiente iteracion y el break sirve para terminar el ciclo
for x in range(0,100):
    if x==10:
        continue
    print(x)

for x in range(0,10):
    if x%2==0:
        continue
    print(x)
