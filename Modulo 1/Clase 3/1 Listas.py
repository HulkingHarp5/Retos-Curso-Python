# Listas
#Elementos que me permiten almacenar varios valores en una sola variable
#Se definen con corchetes []

mi_lista = [1,2,3]
lista1 = [1, "Hola", True, 3.14]

print(mi_lista)

materiales= ["madera", "metal", "plástico"]
print(materiales)

#Las listas pueden tener elementos de diferentes tipos de datos
lista2 = [1, "Hola", True, 3.14]
print(lista2)

#Las listas pueden contener otras listas
lista3 = [1,2,3,["Hola", "Adiós"], 4,5]
print(lista3)

#Con las listas podemos ver qué elementos tienen, cuántos elementos tienen, etc.
#El primer elemento de una lista está en la posición 0
lista_anidada = [1,2,[2,4,6],3]
print(lista_anidada)

print("Primer elemento de la lista mi_lista:", mi_lista[0])
print("Segundo elemento de la lista materiales:", materiales[1])
print("Ultimo elemento de la lista lista2:", lista2[-1]) #-1 es el último elemento
