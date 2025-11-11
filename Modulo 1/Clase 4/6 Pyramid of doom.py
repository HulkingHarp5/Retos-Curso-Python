

# Pyramid of doom
# Se refiere a una estructura de código donde múltiples declaraciones condicionales (if) están anidadas unas dentro de otras, creando una "pirámide" visualmente compleja y difícil de leer.

temperatura_reactor = 105
if temperatura_reactor > 100:  
    print("🔴 ¡Alerta! La temperatura del reactor ha superado el límite crítico. Activando sistema de enfriamiento.") 
    presion_reactor = 250
    if presion_reactor > 200:
        print("🔴 ¡Alerta! La presión del reactor ha superado el límite crítico. Activando válvulas de alivio.")
        nivel_radiacion = 80
        if nivel_radiacion > 50:
            print("🔴 ¡Alerta! Nivel de radiación peligroso detectado. Iniciando protocolo de evacuación.")
            sistema_enfriamiento = False
            if not sistema_enfriamiento:
                print("🔴 ¡Alerta! El sistema de enfriamiento ha fallado. Activando sistema de respaldo.")
                print("⚠️ Múltiples sistemas críticos han fallado. Notificando al equipo de emergencia.")
                print("... el programa continúa su ejecucuón normal.")
print("... el programa continúa su ejecucuón normal.")
# Aunque el código funciona, la estructura anidada hace que sea difícil de leer y mantener.