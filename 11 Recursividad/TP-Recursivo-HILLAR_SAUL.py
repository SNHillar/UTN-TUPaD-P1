def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
    
def calculo_factorial():
    print("=====================")
    n = int(input("Ingrese un número entero no negativo para calcular los factoriles: "))
    print("=====================")
    while n < 0:
        print("El número debe ser no negativo.")
        n = int(input("Ingrese un número entero no negativo: "))
    for i in range(1, n + 1):
        resultado = factorial(i)
        print(f"El factorial de {i} es: {resultado}")

calculo_factorial()


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("=====================")

    
fibonacci_n = int(input("Ingrese un número entero positivo para calcular la serie de Fibonacci: "))
while fibonacci_n < 0:
    print("El número debe ser positivo.")
    fibonacci_n = int(input("Ingrese un número entero positivo para calcular la serie de Fibonacci: "))
    
print("Serie de Fibonacci:")
for i in range(fibonacci_n):
    print(fibonacci(i), end=" ")
    
    
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


print("=====================")    
def calculo_potencia():
    print("Cálculo de Potencia")
    print("=====================")
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = potencia(base, exponente)
    print(f"{base} elevado a {exponente} es: {resultado}")
    
calculo_potencia()


def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
print("=====================")

def calculo_binario():
    print("Conversión de Decimal a Binario")
    print("=====================")
    decimal = int(input("Ingrese un número entero no negativo para mostrar su representación en binario: "))
    while decimal < 0:
        print("El número debe ser no negativo.")
        decimal = int(input("Ingrese un número entero no negativo: "))
    binario = decimal_a_binario(decimal)
    print(f"El número {decimal} en binario es: {binario}")

calculo_binario()

def es_palindromo(palabra):
    palabra = palabra.lower()
    if len(palabra) <= 1:
        return True
    else:
        return palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])
    
print("=====================")
def calculo_palindromo():
    print("Verificación de Palíndromo")
    print("=====================")
    palabra = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")
    if es_palindromo(palabra):
        print(f"{palabra} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")
        
calculo_palindromo()


def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
    
print("=====================")

def calculo_suma_digitos():
    print("Suma de Dígitos")
    print("=====================")
    numero = int(input("Ingrese un número entero positivo para calcular la suma de sus dígitos: "))
    while numero < 0:
        print("El número debe ser positivo.")
        numero = int(input("Ingrese un número entero positivo: "))
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

calculo_suma_digitos()




def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)
    
def calcular_piramide():
    print("Cálculo de Bloques en una Pirámide")
    print("=====================")
    n = int(input("Ingrese el número de bloques en la base de la pirámide: "))
    while n < 0:
        print("El número debe ser no negativo.")
        n = int(input("Ingrese el número de bloques en la base de la pirámide: "))
    total_bloques = contar_bloques(n)
    print(f"El total de bloques en la pirámide es: {total_bloques}")
    

calcular_piramide()



def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
    
def calcular_contar_digito():
    print("Cálculo de la Cantidad de Dígitos")
    print("=====================")
    numero = int(input("Ingrese un número entero positivo: "))
    while numero < 0:
        print("El número debe ser positivo.")
        numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese un dígito (0-9): "))
    while digito < 0 or digito > 9:
        print("El dígito debe estar entre 0 y 9.")
        digito = int(input("Ingrese un dígito (0-9): "))
    resultado = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")


calcular_contar_digito()


