import estructuras
import paquete

##############################################   PISCOYA TIRADO JOSÉ LUIS   ##################################################
dic=estructuras.capitales

print("Ingrese el país")
print("Opciones: Francia,Chile,España")
n=str(input())
print("La capital es: ",dic.get(n))


print("Siguiente proceso?  1) SI   2) No")
print("Escriba el número de la opción")

x=int(input())

if(x==1):
    print("____________________________")
    print("Tabla de Precios")
    print("MANZANA: S/.",estructuras.producto.get("Manzana"),".00")
    print("CHOCOLATE: S/.",estructuras.producto.get("Chocolate"),".00")
    print("JUGUETE S/.",estructuras.producto.get("Juguete"),".00")
    print("AGUA: S/.",estructuras.producto.get("Botella de Agua"),".00")
    print("_____________________________")

print("Ahora un Juego............")
print("Adivina el número del 1 al 10")

print("Ingrese el primer num")
n1 = int(input())

print("Ingrese el segundo num")
n2 = int(input())

print("El resultado es: ", paquete.adivina(n1,n2))