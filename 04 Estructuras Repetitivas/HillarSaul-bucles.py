#1. 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 


"""for num in range(0, 101):
    print(num)"""


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

"""numUsuario = int(input("Ingresa un número por favor: "))

contador = 0

for digit in str(numUsuario):
    contador += 1
    
print("La cantidad de dígitos es:", contador)"""

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 

"""num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

suma = 0 #inicializamos la variable que va a almacenar todos lo valores en cada iteración.

for num in range(num1 + 1, num2): #excluyo los dos valores ingresados por el usuario
    suma += num #sumo los valores entre medio, con la variable sumatoria

print("La suma de los números entre", num1, "y", num2, "es:", suma) #imprimo el resultado final"""


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0. 

"""num = int(input("Ingresa un número (0 para terminar): "))
total = 0

while num != 0:
    total += num
    num = int(input("Ingresa un número (0 para terminar): "))

print("El total acumulado es:", total)"""

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


"""import random

print("Bienvenido a mi juego de adivinanza!")
print("El juego consiste en adivinar un número aleatorio entre 0 y 9.")

numAleatorio = random.randint(0, 9)

numIngresado = -1

intentos = 0

while numIngresado != numAleatorio:
    intentos += 1
    numIngresado = int(input("Intenta adivinar el número: "))

print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")"""

"""#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

for numPar in range(100, -1, -2): #creamos un for, pasando por parámetro un intervalo de -2 para iterar.
    print(f"Los números pares desde 100 a 0 en orden decreciente son: {numPar}")"""
    
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.

"""calculoSuma = 0

numEntero = int(input("Ingresa un número entero positivo: "))


for num in range(0, numEntero + 1):
    calculoSuma += num
print("La suma de todos los números es:", calculoSuma)
"""

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

"""numerosIngresados = 0
pares = 0
impares = 0
negativos = 0
positivos = 0

while numerosIngresados < 100:
    num1 = int(input("Ingrese un número: "))
    if num1 % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num1 < 0:
        negativos += 1
    else:
        positivos += 1
    numerosIngresados += 1
    
print(f"La cantidad de pares son: {pares}")
print(f"La cantidad de impares son: {impares}")
print(f"La cantidad de negativos son: {negativos}")
print(f"La cantidad de positivos son: {positivos}")"""

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

"""nums = 0

media = 0

suma = 0

while nums < 10:
    numero = int(input("Ingrese un valor: "))
    suma += numero
    nums += 1

media = suma / nums
print("La media de los valores ingresados es:", media)"""



#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingresa un número: ")

numeroInvertido = ""

for num in numero:
    numeroInvertido = num + numeroInvertido
    numero = int(numero) // 10
print("El número invertido es:", numeroInvertido)