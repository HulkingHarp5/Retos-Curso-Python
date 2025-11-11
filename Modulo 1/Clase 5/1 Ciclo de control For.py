
# ---Función For---

secuencia = [1,2,3,4,5]
#¿Cuál es la foma más sencilla de imprimir todos los elementos de una lista?

#manera difícil:
print("Manera difícil:")
print(secuencia[0])
print(secuencia[1])
print(secuencia[2])
print(secuencia[3])
print(secuencia[4])

#manera fácil:
print("Manera fácil (for):")
for elemento in secuencia:  #For requiere dos variables, una para iterar y otra para el objeto a iterar
    print(elemento) 

#Prueba Personal
secuencia_prueba = ["Marco, Antonio, Magaña, Soriano"]
secuencia2 = secuencia_prueba[0].split(", ")    #! Uso de .split con cadena de carácteres
for elem in secuencia2:
    print(elem)


