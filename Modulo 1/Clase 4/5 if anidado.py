bateria_porcentaje = 85
motor_activado = True
altitud_metros = 60

print("Iniciando sistema de monitoreo del dron...")
bateria_porcentaje = int(input("Ingrese el porcentaje actual de la batería (0-100): "))
bateria_porcentaje = int(input("Dime el porcentaje de bateria que tiene tu dron: "))
motor_activo = input("El motor esta activo? (si/no): ")
if motor_activo.lower() == "si":   #! Uso de .lower
    motor_activo = True
else:
    motor_activo = False
altitud_metros = int(input("Dime la altitud en metros a la que esta volando el dron"))
print("--- Iniciando diagnóstico del Dron ---")

# --- PRIMER NIVEL DE DECISIÓN: ¿Hay suficiente batería? ---
if bateria_porcentaje > 20:
    print(f"✅ Batería OK ({bateria_porcentaje}%)")

    # --- SEGUNDO NIVEL DE DECISIÓN: ¿Están los motores activos? ---
    # Este bloque 'if/else' está ANIDADO dentro del primer 'if'.
    # Solo se ejecuta si la batería está OK.
    
    if motor_activo == True:
        print("  ✅ Motores Activos.")

        # --- TERCER NIVEL DE DECISIÓN: Evaluar la altitud de vuelo ---
        # ¡Podemos anidar aún más profundo!
        
        if altitud_metros > 100:
            print(f"  🔴 ALERTA: Altitud excesiva ({altitud_metros}m). Descendiendo.")
        elif altitud_metros > 50:
            print(f"  🟡 PRECAUCIÓN: Altitud elevada ({altitud_metros}m). Manteniendo posición.")
        else:
            print(f"  ✅ Altitud segura ({altitud_metros}m).")

    else: # else del segundo nivel
        print("  🟡 ALERTA: Batería OK, pero los motores están inactivos.")

else: # else del primer nivel
    print(f"🔴 CRÍTICO: Batería baja ({bateria_porcentaje}%). Imposible despegar. Aterrizando de emergencia.")

print("--- Diagnóstico Finalizado ---")