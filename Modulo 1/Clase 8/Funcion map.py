#usos de la funcion map
numeros = [1, 2, 3, 4, 5]

# Queremos una lista con el doble de cada número
# map(funcion_a_aplicar, lista_de_datos)
#! Toma una lista y una función. 
#! Luego, aplica la función a cada uno de los elementos y te devuelve una nueva lista con los resultados de esas aplicaciones.
dobles = map(lambda x: x * 2, numeros)

# map() devuelve un objeto 'map', lo convertimos a lista para verlo
print(list(dobles))

#funcion filter
#! Toma una lista y una función de "prueba" (una función que devuelve True o False). 
#! Recorre cada elemento, le hace la prueba, y te devuelve una nueva lista solo con los elementos que pasaron la prueba (los que dieron True)
numeros = [10, 5, 22, 1, 8, 30]

# Queremos una lista solo con los números mayores a 10
# filter(funcion_condicion, lista_de_datos)
mayores_a_10 = filter(lambda x: x > 10, numeros)

print(list(mayores_a_10))

# función es aquella que recibe unos parámetros (o no) y devuelve un valor.
# Ejemplo de función: print(), input(), len(), type(), int(), float(), str(), etc.

# Sentencia es aquella que realiza una acción, como asignar un valor o imprimir algo.
# Ejemplo de sentencia: asignaciones (a = 5), estructuras de control (if, for, while), llamadas a funciones (print("Hola"))