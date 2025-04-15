from statistics import mean, median, mode #importando libreria para el ejercicio 6
import random #importando libreria para el ejercicio 6



#Ejercicio 1: Crear un programa que pida al usuario su edad.

edad = int(input("¿Cuál es tu edad? "))

if edad > 18:
    print("Eres mayor de edad")
    
#Ejercicio 2:

nota = int(input("¿Cuál es tu nota? "))
if nota == 6:
    print("Aprobado")
else:
    print("Reprobado")
    
#Ejercicio 3:

soloPares = int(input("Ingrese solo npumeros pares: "))

if soloPares % 2 == 0:
    print("Ha ingresado un número par")
    
else:
    print("Por favor, ingrese un número par")
    
#Ejercicio 4:

edadNino = int(input("¿Cuál es la edad del niño? "))
if edadNino < 12:
    print("El niño es menor de edad")
elif edadNino >= 12 and edadNino < 18:
    print("Eres adolescente")
elif edadNino >= 18 and edadNino < 30:
    print("Eres joven")
else:
    print("Eres adulto")
    
#Ejercicio 5:
password = input("Ingrese su contraseña: ")

if len(password) <= 8 and len(password) <= 14:
    print("La contraseña es válida")
else:
    print("La contraseña debe tener entre 8 y 14 caracteres")

#Ejercicio 6:

numerosAleatorios = [random.randint(1, 100) for _ in range(50)]

moda = mode(numerosAleatorios) 
print("La moda es:", moda)
media = mean(numerosAleatorios)
print("La media es:", media)
mediana = median(numerosAleatorios)
print("La mediana es:", mediana)
print("Los números aleatorios son:", numerosAleatorios)

if media > mediana and mediana > moda:
    print("Sesgo a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo a la izquierda")
elif media == mediana and mediana == moda:
    print("Distribución normal")
else:
    print("Distribución no normal")
    
    
    
#Ejercicio 7:

frase = input("Ingrese una frase: ")
terminaVocal = len(frase) - 1

if frase[terminaVocal] in "aeiou":
    frase = frase + "!"
    print("La frase es:", frase)
else:
    print(frase)
    
#Ejercicio 8:

nombre = input("Ingrese su nombre: ")


print ("""------------------------------------------------------
    Ingrese:
    • 1 para mostrar su nombre en mayúsculas
    • 2 para mostrar su nombre en minúsculas
    • 3 para mostrar su nombre con la primera letra en mayúscula y el resto en minúsculas
    
    
    ------------------------------------------------------
    """)

opcion = int(input("Ingrese una opción: "))

if opcion == 1:
    print(nombre.upper()) #para convertir a mayusculas
elif opcion == 2:
    print(nombre.lower()) #para convertir a minusculas
elif opcion == 3:
    print(nombre.capitalize()) #pasa la primera letra a mayuscula y el resto a minusculas
else:
    print("Opción no válida")



magnitudTerremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitudTerremoto < 3:
    print("Muy leve")
elif magnitudTerremoto >= 3 and magnitudTerremoto < 4:
    print("Leve")
elif magnitudTerremoto >= 4 and magnitudTerremoto < 5:
    print("Moderado")
elif magnitudTerremoto >= 5 and magnitudTerremoto < 6:
    print("Fuerte")
elif magnitudTerremoto >= 6 and magnitudTerremoto < 7:
    print("Muy fuerte")
elif magnitudTerremoto >= 7:
    print("Extremo")
else:
    print("Magnitud no válida")
    
#Ejercicio 10:


hemisferio = input("Ingrese el hemisferio (N/S): ").upper()

ingreseDia = int(input("Ingrese el día: "))
ingreseMes = int(input("Ingrese el mes: "))

if ingreseDia > 1 and ingreseDia < 31 and ingreseMes > 1 and ingreseMes < 12:
    if hemisferio == "N":
        if ingreseMes >= 3 and ingreseMes <= 5:
            print("Es primavera")
        elif ingreseMes >= 6 and ingreseMes <= 8:
            print("Es verano")
        elif ingreseMes >= 9 and ingreseMes <= 11:
            print("Es otoño")
        else:
            print("Es invierno")
    elif hemisferio == "S":
        if ingreseMes >= 3 and ingreseMes <= 5:
            print("Es otoño")
        elif ingreseMes >= 6 and ingreseMes <= 8:
            print("Es invierno")
        elif ingreseMes >= 9 and ingreseMes <= 11:
            print("Es primavera")
        else:
            print("Es verano")
    else:
        print("Hemisferio no válido")
else:
    print("Fecha no válida")
    


