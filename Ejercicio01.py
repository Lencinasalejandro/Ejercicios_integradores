# 1. Escribir una función que calcule el máximo común divisor entre dos números.

def maximo_comun_divisor(numero1,numero2):
    if  numero1 == 0:
        if numero2 == 0:
            print("Ambos numeros son 0, no hay Maximo comun denominador.")
        else:
            print("El maximo comun denominador es ",numero2)
            return numero2
    else:
        if numero2==0:
            print("El maximo comun denominador es ",numero1)
            return numero1
        elif numero1==numero2:
            print("El maximo comun denominador es ",numero2)
            return numero2
        else:
            if (numero1>numero2):
                end=numero2
            else:
                end=numero1
            aux=1
            while(aux<=end):
                aux1=numero1%aux
                aux2=numero2%aux
                if((aux1==0) and (aux2==0)):
                    mcd=aux
                aux+=1
            return mcd
            
numero1=int(input("Ingrese el primer valor.\n"))
numero2=int(input("Ingrese el segundo valor.\n"))
mcd=maximo_comun_divisor(numero1,numero2)
print("El maximo comun denominador es ",mcd)