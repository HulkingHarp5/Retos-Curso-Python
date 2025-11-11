mediciones_de_voltaje=[12.5, 12.1, 12.7, 12.4, 12.6]
suma_total = 0.0 #Creamos el acumulador fuera del bucle

for voltaje in mediciones_de_voltaje:
    #Actualizamos el acumulador dentro del bucle
    suma_total += voltaje #suma_total = suma_total + voltaje
    print(f"Voltaje actual: {voltaje}, Suma total acumulada: {suma_total}")

#Usamos el resultado fuera del bucle
cantidad_mediciones = len(mediciones_de_voltaje)
promedio = suma_total / cantidad_mediciones

print(f"\nResultados finales:")
print(f"Suma total de voltajes: {suma_total}")
print(f"El voltaje promedio es: {promedio: .2f} V") #! .2f limita a 2 decimales