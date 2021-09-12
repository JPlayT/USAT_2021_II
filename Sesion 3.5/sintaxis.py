

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

   