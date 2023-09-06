frase = input("Ingrese frase: ")
caracter = input("Ingrese letra: ")
repeticiones=0

for l in frase:
    if caracter==l:
        repeticiones+=1
print(f"la letra {caracter} se repite {repeticiones} veces")

#Equipo expuso
