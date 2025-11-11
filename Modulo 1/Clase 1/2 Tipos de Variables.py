entero = 10
flotante = 10.5
cadena = "Hola"
booleano = True
lista = [1, 2, 3]
tupla = (1, 2, 3)
Conjunto = {1, 2, 3}
diccionario = {"clave": "valor"}

"""
Se utiliza la función type() para conocer el tipo de dato de una variable.
"""
print(type(entero))
print(type(flotante))
print(type(cadena))
print(type(booleano))
print(type(lista))
print(type(tupla))
print(type(Conjunto))
print(type(diccionario))

print(entero)
print(flotante)
print(cadena)
print (booleano)
print(lista)
print(tupla)
print(Conjunto)
print(diccionario)

"""
Conversión de variables
"""

a = 5
b = 2.5
c = "3"

print(a + b + int(c))  # Convierte c a entero para la suma
print(a + b + float(c)) # Convierte c a flotante para la suma
print(str(a) + str(b)+c) # Convierte a y b a cadena para la concatenación
# Una concatenación es cuando se unen dos tipos de datos cadena


"""
Inputs y Outputs
"""

print("Hola, usuario!. Ingresa tu nombre")  # Output básico
nombre = input()  # Input básico
print("Hola," + nombre + " Bienvenido al curso de Python")  # Output con variable

# Otraa forma de usar input

nombre = input("Ingresa tu nombre: ")  # Input con mensaje
print("Hola," + nombre + " Bienvenido al curso de Python")  # Output con variable

# Función print f

print("Hola, usuario!. Ingresa tu nombre")  # Output básico
nombre = input()  # Input básico
print(f"Hola, {nombre} Bienvenido al curso de Python")  # Output con variable usando f

edad = int(input("Ingresa tu edad: "))  # Input con conversión a entero
print(f"Tu edad es {edad} años")  # Output con variable usando f

# Usamos "Cls" para limpiar la consola de comandos