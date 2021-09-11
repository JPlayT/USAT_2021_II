#Piscoya Tirado José Luis


# Una lista es una estructura de datos que contiene una colección o secuencia de datos mutable, es decir permite agregar y quitar objetos.
estaciones= ["Primavera","Verano","Otoño","Invierno",5,4,3,2,1]
frutas= ["Pera","Palta","Uva",["Uva sin pepa","Uva con pepa"],5,4,3,2,1]
print(estaciones)
print(frutas)

# Una tupla permite tener agrupados un conjunto inmutable de elementos, es decir, en una tupla no es posible agregar ni eliminar elementos.
TuplaDiasSemana = ("LU", "MA", "MI", "JU","VI", "SA", "DO")
print(TuplaDiasSemana)
edades = (11,32,41,12,42,10,6)
print(edades)

# Un conjunto es una lista de elementos sin posición, en donde no se puede acceder mediante el index.
setUtensilios = {"Tenedor","Cuchara","Cuchillo","Palillos"}
frutas= {"Pera","Palta","Uva","Naranja"}
print(setUtensilios)
print(frutas)

# Los diccionarios son objetos que contienen una lista de parejas de elementos. De cada pareja un elemento es la clave, que no puede repetirse, y, el otro, un valor asociado.
capitales = {"Chile":"Santiago", "España":"Madrid", "Francia":"París"}
print(capitales)
capitales = {"Chile":"Santiago", "España":"Madrid", "Francia":"París","Francia":"Torre"} #El último valor que se le asigna al mismo id en un diccionario reemplaza al anterior.
print(capitales)