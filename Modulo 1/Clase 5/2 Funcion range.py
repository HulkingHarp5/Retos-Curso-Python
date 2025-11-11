
# ---Función range---
#Range sirve para generar una secuencia de números en un rango específico, muy útil para ciclos for
print("Iniciando prueba 5 de ciclos del motor: ")

# 'i' (de índice) es el nombre standard para contadores
for i in range(5) :
    print(f"Ciclo de prueba número {i+1} ")

# Si nosotros queremos un rango específico, podemos indicarlo en la función range (inicio, fin)
print("\nProbano ciclos del motor del 3 al 7: ")
for i in range(3,8):
    print(f"Ciclo de prueba número {i} ")

# También podemos iniciar un paso diferente al 1
print("\nProbando ciclos del motor del 2 al 10, de 2 en 2: ")
for i in range(2,11,2): # (inicio, fin, salto)
    print(f"Ciclo de prueba número {i} ")