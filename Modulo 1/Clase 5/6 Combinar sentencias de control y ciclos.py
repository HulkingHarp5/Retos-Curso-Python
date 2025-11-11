
# Combinar sentencias if con bucles for
mediciones_ph=[7.1, 7.3, 6.4, 7.0, 7.6, 7.2, 5.9]
conteo_anomalias = 0
anomalias_detectadas = []
mediciones_ph.sort() #!

print(f"PH: {mediciones_ph}")
print("\n---Inicializando monitor de calidad de PH---")
for ph in mediciones_ph:
    # Este if se ehecuta cada iteración
    if ph < 6.5 or ph > 7.5: # El or se usa para combinar dos condiciones
        print(f"Alerta: Medición de PH anómala detectada: {ph}")
        conteo_anomalias += 1
        anomalias_detectadas.append(ph)
        anomalias_detectadas.sort() #!
        
print(f"\n---Monitoreo completado---")
print(f"Total de mediciones: {len(mediciones_ph)}")
print(f"Total de anomalías detectadas: {conteo_anomalias}")
print(f"Anomalías detectadas: {anomalias_detectadas}")
