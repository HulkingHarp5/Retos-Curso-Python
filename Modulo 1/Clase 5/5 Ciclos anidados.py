
# Anidar ciclos for dentro de otros ciclos
for i in range(1,4):
    print(f"Ciclo externo: i={i}")
    for j in range(1,4):
        print(f"Ciclo interno j={j}")
    print() # Línea en blanco para separar las iteraciones del ciclo externo

    # Ejemplo de anidamiento de ciclo for en Python
temperaturas = [50, 75, 100]
presiones = [10, 20]

print("--- Inicializando Simulación de Pruebas de Material ---")

#! REVISAR HASTA ENTENDER
# Bucle exterior controla temperatura 
# Se ejecutará 3 veces
for temp in temperaturas:
    print(f"\n---Pruebas a {temp}°C ---")

    # Bucle interior controla presión
    # Por cada temperatura, se ejecutará 2 veces
    for pres in presiones:
        # Este código se ejecuta 6 veces en total (3 temperaturas x 2 presiones)
        print(f"Realizando prueba a {temp}°C y {pres} psi...")
        # Aquí se podría agregar código para simular la prueba
print("\n--- Simulación de Pruebas Completada ---")