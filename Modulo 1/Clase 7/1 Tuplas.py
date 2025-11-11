
# Tuplas
# Son estructuras de datos que permiten almacenar varios valores en una sola variable
# A diferencia de las listas, las tuplas son inmutables (no se pueden modificar después de su creación)
# Se definen utilizando paréntesis ()

cordenadas = (10.0, 20.0)
print(cordenadas)

# Pueden contener diferentes tipos de datos
persona = ("Juan", 30, 1.75)
print(persona)

# Se puede acceder a los elementos de una tupla mediante índices
print("Nombre:", persona[0])
print("Edad:", persona[1])
print("Estatura:", persona[2])

# Desempaquetado de tuplas
nombre, edad, estatura = persona
print("nombre:", nombre)
print("edad:", edad)
print("estatura:", estatura)

# Concatenación de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)

# Repetición de tuplas
tupla_repetida = tupla1 * 3
print("Tupla repetida:", tupla_repetida)

# También tienen metodos como count() y index()
numeros = (1, 2, 3, 2, 4, 2)
print("Número de veces que aparece el 2:", numeros.count(2))
print("Índice del primer 3:", numeros.index(3))
#! Las tuplas son útiles cuando se desea almacenar datos que no deben cambiar durante la ejecución del programa.