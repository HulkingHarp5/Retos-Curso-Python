# Reto 1:

# Crea una clase llamada "Componente"
class Componente:

    # Crear el Constructor
    def __init__(self, NS, tipo_componente, costo):

        # Definir Atributos
        self.NS = NS 
        self.tipo_componente = tipo_componente
        self.costo = costo 

        # Atrinutos por defecto
        self.historial_revisiones = []
        self.esta_activo = True

# Crear Instancias de la Clase Componente
c1 = Componente("MTR-101", "Motor", 550.75)
c2 = Componente("SNR-2050", "Sensor", 80.20)

# Modificar Atributos de las Instancias
c1.historial_revisiones.append("2025-01-15: Revisión completa")
c2.historial_revisiones.append("2025-02-10: Sustitución de pieza")
c2.esta_activo = False

# Inmprimir Reporte
print("\n=== Revisión de Componentes ===")
print(f"\nComponente 1:\nNúmero de Serie: {c1.NS}\nTipo: {c1.tipo_componente}\nCosto: ${c1.costo}\nHistorial de Revisiones: {c1.historial_revisiones}\nActivo: {c1.esta_activo}")
print(f"\nComponente 2:\nNúmero de Serie: {c2.NS}\nTipo: {c2.tipo_componente}\nCosto: ${c2.costo}\nHistorial de Revisiones: {c2.historial_revisiones}\nActivo: {c2.esta_activo}")
