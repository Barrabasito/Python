#Escribir un programa que pregunte el nombre de un producto, su precio y su numero de unidades, 
# y mostrar en pantalla una cadena cual nombre del producto, seguido del precio unitario de 6 digitos enteros 
# y dos decimales, el numero de unidades con tres digitos y el costo total con 8 digitos enteros y dos decimales.

#Nombre del producto
strNombre=input("Teclee el nombre del producto: ")
flPrecio=float(input("Teclee el precio del producto: "))
intNumeroUnidades=int(input("Escriba el numero de unidades: "))

precioUnitario=str(format(flPrecio, '.2f')).zfill(9)
costoTotal=str(format(intNumeroUnidades*flPrecio, '.2f')).zfill(11)
                      
print(f"Nombre del producto: {strNombre}\nPrecio unitario: {precioUnitario}\nNumero de unidades: {str(intNumeroUnidades).zfill(3)}\nCosto total: {costoTotal}")