# ) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
#  range. 

mi_lista = list(range(4, 101, 4))
print(mi_lista)

#2)

lista_5_elementos = [1, "Jorge", 3.14, True, False]
print(lista_5_elementos[-2]) # Imprime el penúltimo elemento de la lista


#3) 

lista_vacia = []

lista_vacia.append("perro") # Agrega el número 1 a la lista vacía
lista_vacia.append("gato")
lista_vacia.append(2)

print(lista_vacia)



#4)

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro" # Agrega el elemento "loro" al final de la lista
animales[-1] = "oso" # Cambia el último elemento de la lista por "oso"
print(animales)

#5) La funcion max(numeros) siendo números una lista de enteros, devuelve el número mayor de la lista. En el ejercicio le pasa el metodo .remove() a la lista, por lo que en la llamada a la función prunt, devuelve la lista, sin el número mayor. (22 en nuestro ejercicio)


#6)

lista_10a30 = list(range(10, 31, 5)) # Crea una lista con los números del 10 al 30

print(lista_10a30[0:2]) # Imprime el primer y segundo elemento de la lista

#7)

autos = ["sedan", "polo", "suran", "gol"] # Crea una lista con los nombres de los autos

autos[1:3] = ["ford", "chevrolet"] # Cambia los elementos de la lista en las posiciones 1 y 2 por "ford" y "chevrolet"
print(autos) # Imprime la lista de autos

#8)

dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)


print(dobles) # Imprime la lista con el número 10


#9)

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
["agua"]]# Crea una lista de listas con los elementos de la compra


compras[2].append("jugo") # Agrega el elemento "gaseosa" a la lista de compras  punto a)

"""print(compras)""" # Imprime la lista de compras

compras[1][1] = "tallarines" # Cambia el segundo elemento de la segunda lista por "tallarines"   punto b)
"""print(compras)""" # Imprime la lista de compras


compras[0].remove("pan") # Elimina el elemento "pan" de la primera lista de compras  punto c)



print(compras) # Imprime la lista de compras d)


#10)

lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]

print(lista_anidada[0])










