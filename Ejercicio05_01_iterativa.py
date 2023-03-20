# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su 
# valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando 
# mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

def get_int():
    while (1):
        cadena=input("Ingrese un numero entero.\n")
        
        if not (cadena.isnumeric()):
            print("El numero ingresado no es entero, intente de nuevo")
        else:
            break
    return(int(cadena))        
        
    
entero=get_int()
print(type(entero))
print(entero)
#Solo positivos