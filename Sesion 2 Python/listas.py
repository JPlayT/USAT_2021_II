#Listas de Python

lista1=["naranja","pera","manzana","melón","piña","maracuyá"]

print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])

print(lista1[1:3]) #3 elementos desde la pos 1
print(lista1[:3]) #3 elementos desde la pos 0
print(lista1[2:]) #3 Todos los elementos desde la pos 2

lista1.append("Lichie")
print(lista1)

lista1.insert(2,"papaya")
print(lista1)

lista1.extend(["guanabana","chimichurri"])
print(lista1)

print(lista1.index("papaya"))

