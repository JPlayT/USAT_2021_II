
def contar(): # método libre, no es necesario instanciar la clase ni el self y puede tener parámetros

    for i in range(1,5): # Cuenta del 1 al 4
        print(i)


class persona:

    def __init__(self): #Constructor sin parámetros
        self.nombre="Anonimo"
        self.edad=9999
        
    def __init__(self,nombre,edad): #Constructor con parámetros
       self.nombre=nombre
       self.edad=edad


    def setNombre(self,nombre): #Ejemplo de setter // Se le puede agregar arreglo de exepciones y condiciones o print
        self.nombre=nombre

    def getNombre(self): #Ejemplo de getter // Tambien se le puede agregar exepciones y condiciones o print
        return self.nombre
    

    def saludar(self,destinatario): #Método de clase, agregar "Self" como parámetro solo si le pertenece a una class
        print(self.nombre,"está saludando a",destinatario)

    def ponteAcontar(self,maximo):
        print(self.nombre,"empieza a contar.")
        for i in range(0,maximo+1):
            print(i)

   