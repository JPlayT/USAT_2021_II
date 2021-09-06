#Creación de Clase llamada MyClass, y propiedad x
# class MyClass:
#     x=5


#Constructor de la clase Person
class Person:

    # "def" crea funciones
    # "self" parabra recerbada
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def miFuncion(self):
        print("Mi nombre es "+ self.name)

#Creacion de obj p1 de la class Person
p1= Person("Oscar",44)

print(p1.name)
print(p1.age)

p1.miFuncion()