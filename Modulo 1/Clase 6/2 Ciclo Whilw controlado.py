
# Ciclo While controlado por contador requiere 3 elementos:
# 1. Inicialización del contador
# 2. Condición del ciclo
# 3. Actualización del contador
#? El contador se inicializa antes dek ciclo,
#? La condición se evalúa en cada iteración del ciclo y
#? El contador se actualiza dentro del ciclo para evitar un ciclo infinito

contador = 1 # Inicialización del contador
suma = 0 #Variable para almacenar la suma de los números
while contador <= 5: # Condición del ciclo
    numero = int(input("Ingrese un número: "))
    suma += numero # Actualización de la suma
    contador += 1 # Actualización del contador
    print(f"Has ingresado {contador-1} números hasta ahora.")
print(f"La suma total de los números ingresados es: {suma}")