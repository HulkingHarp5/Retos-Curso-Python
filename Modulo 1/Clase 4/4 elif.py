
# elif sirve para manejar múltiples condiciones de manera más eficiente.
rpm = int(input("Ingrese las RPM del motor: "))

#Inspección completa con múltiples condicionales
if rpm > 2500:
    print("🔴 RPM demasiado altas. Reduzca la velocidad inmediatamente.")
elif rpm > 1800:
    print("🟠 RPM altas. Considere reducir la velocidad.")
elif rpm > 600:
    print("🟢 RPM normales. El motor")
elif rpm > 0:
    print("🟡 RPM bajas. Aumente la velocidad para un rendimiento óptimo.")
else:
    print("⚫ Motor apagado.")