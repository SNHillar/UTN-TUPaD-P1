""" def imprimir_hola_mundo():
    return print("Hola Mundo")
    
    
imprimir_hola_mundo()

def saludar_usuario(nombre):
    return print(f"Hola, {nombre}!")

nombre1 = input("¿Cuál es tu nombre? ")

saludar_usuario(nombre1) #llamamos a la función saludar_usuario


def informacion_personal(nombre, apellido,edad, residencia):
    return print(f"Hola, {nombre} {apellido}, tienes {edad} años y vives en {residencia}.")

nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuál es tu edad? ")
residencia = input("¿Cuál es tu residencia? ")

informacion_personal(nombre, apellido, edad, residencia) #llamamos a la función informacion_personal, pidiendo los datos al usuario """

""" import math

def calcular_area_circulo(radio):
    pi = math.pi
    area = pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    pi = math.pi
    perimetro = 2 * pi * radio
    return perimetro


radio = float(input("¿Cuál es el radio del círculo? "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo con radio {radio} es: {area} y el perímetro es: {perimetro}") """


""" def segundos_a_horas(segundos):
    horas = segundos // 3600
    return print(f"{segundos} segundos son {horas} horas")
    
segundos = int(input("¿Cuántos segundos quieres convertir a horas? "))

segundos_a_horas(segundos) """

""" 
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("¿Qué número quieres multiplicar? "))
tabla_multiplicar(numero) """

""" def operaciones_basicas(a, b):
    suma = (a + b)
    resta = (a - b)
    multiplicacion = (a * b)
    division = a / b if b != 0 else "Error: División por cero" #tiene un condicional para evitar la división por cero
    return suma, resta, multiplicacion, division #esto devuelve una tupla con los resultados de las operaciones

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

resultados = operaciones_basicas(a, b) #llamamos a la función operaciones_basicas con la tupla de resultados

#desempaquetamos la tupla de resultados, accediendo a cada uno de los resultados con su índice
# y los imprimimos
#en la consola
print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicación:", resultados[2])
print("División:", resultados[3]) """


""" def calcular_imc(peso, altura):
    peso = float(peso)
    altura = float(altura)
    imc = peso / (altura ** 2)
    return imc

peso = input("¿Cuál es tu peso en kg? ")
altura = input("¿Cuál es tu altura en metros? ")
imc = calcular_imc(peso, altura)

print(f"Tu IMC es: {imc:.2f}") #esto imprime el IMC con 2 decimales """


""" def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp = float(input("¿Cuál es la temperatura en Celsius? "))
temp_fahrenheit = celsius_a_fahrenheit(temp)
print(f"La temperatura {temp}° en Fahrenheit es: {temp_fahrenheit:.2f}") #esto imprime la temperatura en Fahrenheit con 2 decimales """

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}") #esto imprime el promedio con 2 decimales

