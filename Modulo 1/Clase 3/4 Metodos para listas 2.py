
lista = [1,2,3]

# Len
print(f"Longitud de la lista: {len(lista)}") #Devuelve la cantidad de elementos en la lista 

# Sort 
lista_numeros = [4,2,1,6,3,5]
print(f"Lista desordenada: {lista_numeros}")
lista_numeros.sort() #Ordena los elementos de la lista en orden ascendente
print(f"Lista ordenada: {lista_numeros}")

# Reverse
lista_numeros.reverse() #Invierte el orden de los elementos en la lista
print(f"Lista invertida: {lista_numeros}")

# Count
lista_duplicados = [1,2,2,3,3,3] 
print(f"Lista con elementos duplicados: {lista_duplicados}")
print(f"El número 2 aparece {lista_duplicados.count(2)} veces en la lista") #Cuenta cuántas veces aparece un elemento en la lista
print(f"El número 3 aparece {lista_duplicados.count(3)} veces en la lista")

# Index
listas = [1,2,3,4,5]
print(f"El índice del elemento 3 es: {listas.index(3)}") #Devuelve el índice del primer elemento con el valor especificado

# Split
videojuegos = "Zelda, Mario, Metroid"
lista_videojuegos = videojuegos.split(", ") #Divide una cadena en una lista usando la coma y el espacio como separador
print(f"Lista de videojuegos: {lista_videojuegos}")


# In
frase = "Hola, bienvenido al curso de Python"
palabras = frase.split(" ") #Divide una cadena en una lista de palabras usando el espacio como separador
print(f"Lista de palabras: {palabras}")
print(f"La palabra 'curso' está en la frase: {'curso' in frase}") #Verifica si un elemento está en la lista o cadena