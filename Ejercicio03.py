#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario 
# con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

cadena=input("Ingrese una cadena de caracteres.\n")
lista=cadena.split(" ")
diccionario={}

for i in lista:
    if(diccionario.__contains__(i)):
        diccionario[i]+=1
    else:
        diccionario[i]=1
print(diccionario)