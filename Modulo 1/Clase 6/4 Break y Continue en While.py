
contador = 0 
while contador < 10:
    contador += 1
    if contador == 7:
        break  # Sale del ciclo cuando contador es 7
    if contador % 2 == 0: # Se lee "si el contador es par"
        continue  # Salta a la siguiente iteración si el contador es par
    print(f"Contador actual: {contador}")
print("Ciclo terminado.")

# O en ejemplos con While True
while True:
    entrada = input("Escribe 'salir' para terminar el bucle: ")
    if entrada.lower() == 'salir':
        break  # Sale del ciclo si el usuario escribe 'salir'
print("Bucle terminado con while")
