def sumar(num1,num2):
    resultado = num1 + num2
    return resultado

def restar(num1,num2):
    return num1-num2

def multiplicar(num1,num2):
    return num1*num2

def dividir(num1,num2):
    return num1/num2

def potencia(num1,num2):
    return num1**num2

def saludo(nombre):
    print("Hola ",nombre)

def adivina(num1,num2):
    import random

    n= random.randint(1,10)
    
    if(num1==n):
        print("Correcto Adivinaste el número")
        return n
    else:

        print("Primer número n1 incorrecto")

        if(num2==n):
            print("Correcto Adivinaste el número con tu segundo intento")
            return n
        else:
            print("Vuelve a intentar")
            return n