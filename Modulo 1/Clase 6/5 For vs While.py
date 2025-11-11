
# Ciclo for iterando sobre una secuencia
# Ciclo while repite un bloque de código mientras una condición sea verdadera
import random
numero_secreto = random.randint(1,10) #Número secreto aleatorio entre 1 y 10

#! For = cuando sabemos cuántas veces queremos repetir un bloque de código
print("Contaremos los número divisibles entre 5 en un rango del 1 al 100")
for numero in range(1,101):
    if numero %5 == 0: #%5 es si el número es divisible entre 5
        print(f"El número {numero} es divisible entre 5")
print(f"Hay {100//5} números divisibles entre 5 en el rango del 1 al 100") #.// es división entera

#! While = cuando no sabemos cuántas veces se repetirá el bloque de código, depende de una condición
print("-"*30)
print("Juguemos un juego, adivina el número secreto entre 1 y 10")
numero_intentos = 0
while True: 
    intentos = int(input("¿En qué número estpy pensando?"))
    if intentos < 1 or intentos > 10:
        print("Bobo, el número debe de estar entre 1 y 10")
        numero_intentos += 1
        continue #Salta a la siguiente iteración si el número no está en el rango
    elif intentos != numero_secreto:
        print("Incorrecto, intenta de nuevo")
        numero_intentos += 1
        continue
    elif intentos == numero_secreto:
        print(f"Felicidades, adivinaste el número secreto {numero_secreto} en {numero_intentos} intentos")
        break #Sale del ciclo si el usuario adivina el número secreto

