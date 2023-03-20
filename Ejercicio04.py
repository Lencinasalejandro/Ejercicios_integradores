# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra 
# que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario 
# generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

cadena=input("Ingrese una cadena de caracteres.\n")

def cadena_a_dicc(str):
    lista=str.split(" ")
    diccionario={}

    for i in lista:
        if(diccionario.__contains__(i)):
            diccionario[i]+=1
        else:
            diccionario[i]=1
    return(diccionario)

def dicc_a_tupla(dicc):
    mayor=0
    for i in dicc:
        if(dicc[i]>mayor):
            mayor=dicc[i]
            key=i
    tupla=(key,mayor)
    return tupla

diccionario=cadena_a_dicc(cadena)
print(type(diccionario))
print(diccionario)

tupla=dicc_a_tupla(diccionario)
print(type(tupla))
print(tupla)