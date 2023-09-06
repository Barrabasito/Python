#Escribir un programa que reciva una cadena de caracteres y devuelva un diccionario con cada caracter que contenga y su frecuencia 
#el key va ser el nombre y el value va ser las veces que se repite

def frecuenciaCaracteres(cadena):
    # Diccionario
    frecuencia = {}
    
    for caracter in cadena:
        if caracter in frecuencia:
            frecuencia[caracter] += 1      
        else:
            frecuencia[caracter] = 1
    return frecuencia

cadena = input("Ingrese una cadena: ")

resultado = frecuenciaCaracteres(cadena)
print("Caracteres y su frecuencia:")
for caracter, frecuencia in resultado.items():
    print(f"'{caracter}': {frecuencia}")
