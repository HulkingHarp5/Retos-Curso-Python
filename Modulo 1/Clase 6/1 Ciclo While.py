
# Ciclo While
# El ciclo while se utiliza para repetir un bloque de código mientras una condición sea verdadera.
bandera = True
while bandera:
    print("El ciclo while se está ejecutando.")
    # Aquí puedes agregar una condición para salir del ciclo
    respuesta = input("¿Deseas continuar? (s/n): ")
    if respuesta.lower != 's':
        bandera = False
print("El ciclo while ha terminado.")

# While condición:
#     Bloque de código a repetir
# Ejemplo de in ciclo while infinito:

while True:
    print("Este ciclo while es infinito. Presiona Ctrl+C para detenerlo.")
    