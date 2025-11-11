
# Break y Continue
# Break se utiliza para salir de un ciclo antes de que la condición del ciclo se vuelva falsa.
# Continue se utiliza para saltar a la siguiente iteración del ciclo, omitiendo el resto del código en la iteración actual.

for numero in range(10):
    if numero == 5:
        break # Sale del ciclo cuando numero es 5
    print(f"Número actual: {numero}")
print("Ciclo terminado con break.")
print("-"*30) 

# La instrucción continue se utiliza para saltar a la siguiente iteración del ciclo.
for numero in range (10):
    if numero %2 == 0: #%2 es si el número es par
        continue # Salta a la siguiente iteración si el número es par
    print(f"Número actual: {numero}")
print("Ciclo terminado con continue.")