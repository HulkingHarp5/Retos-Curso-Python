# Append
lista = [1,2,3]
print(lista)
lista.append(74) #Agrega un elemento al final de la lista
print(lista)

# Remove
lista.remove(2) #Elimina el primer elemento con el valor especificado ya sea número o string
print(lista)

# Pop
elemento_eliminado = lista.pop(0) #Elimina el elemento en la posición especificada y lo devuelve
print("Elemento eliminado:", elemento_eliminado)
print("Lista después de .pop:", lista)

# Insert
lista.insert(1,10) # x,y siendo x la posición, y el valor a insertar
print("Lista después de .insert:", lista)
lista_duplicados = [1,2,2,3,3,3]
lista_duplicados.clear() #Elimina todos los elementos de la lista

# Extend
lista1 = [1,2,3]
lista2 = [4,5,6]
lista1.extend(lista2) #Agrega los elementos de lista2 al final de lista1
print("Lista extendida: ", lista1)
