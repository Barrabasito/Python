x=5
while x>0:
    x-=1
    print(x)

x=5
y=0
while x>0 or y<5:
    y+=1
    x-=1
    print(x,y)
else:
    print("Fin del ciclo")
    #Solo si termina todos los ciclos     
    
    #Este es el try catch
try:
    s={1,2,3}
    s[2]=10
except Exception as e:
    print(e)
print("Fin del codigo")