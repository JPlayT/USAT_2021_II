import paquete

print("Ingrese el máximo a contar")
aux=int(input())
print("__________________________")
paquete.contar(aux)

print("Ingrese a quien Saludar")
aux=input()
paquete.saludar(aux)

print("Lista de Animales")
paquete.Animales()

print("Ingrese el primer número: base")
num1=int(input())

print("Ingrese el segundo número: exponente")
num2=int(input())

paquete.calculadoraPotenciacion(num1,num2)

print("________________________________________________")

paquete.Despedida()
