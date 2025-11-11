# Reto 8:

# Diccionario principal vacío
base_de_partes = {}  

# Tupla global de componentes válidos
COMPONENTES_VALIDOS = ("Motor", "Sensor", "Batería", "Chasis")

#! Funciones
def registrar_parte():
    # Registra una nueva pieza en la base de datos
    global base_de_partes

    sn = input("Ingrese el número de serie (S/N): ").strip()
    if sn in base_de_partes:
        print("⚠️ Error: Ese número de serie ya está registrado.")
        return

    print(f"Componentes válidos: {COMPONENTES_VALIDOS}")
    tipo = input("Ingrese el tipo de componente: ").strip().capitalize()
    if tipo not in COMPONENTES_VALIDOS:
        print("⚠️ Error: Tipo de componente no válido.")
        return

    resultados = []
    for i in range(3):
        while True:
            try:
                val = float(input(f"Ingrese resultado de prueba {i + 1} (0-100): "))
                if val < 0 or val > 100:
                    print("⚠️ Ingrese un número entre 0 y 100.")
                    continue
                resultados.append(val)
                break
            except ValueError:
                print("⚠️ Error: Ingrese solo números válidos.")

    base_de_partes[sn] = {
        "tipo_componente": tipo,
        "resultados_pruebas": resultados,
        "estado": "Pendiente"
    }

    print(f"✅ Pieza {sn} registrada exitosamente.")


def buscar_parte():
    # Busca una pieza por su número de serie
    sn = input("Ingrese el número de serie (S/N) a buscar: ").strip()
    parte = base_de_partes.get(sn)

    if parte:
        print(f"Tipo: {parte['tipo_componente']}")
        print(f"Resultados: {parte['resultados_pruebas']}")
        print(f"Estado: {parte['estado']}")
    else:
        print("⚠️ No se encontró ninguna parte con ese número de serie.")


def evaluar_parte():
    # Evalúa una pieza y cambia su estado según el promedio
    sn = input("Ingrese el número de serie (S/N) a evaluar: ").strip()
    parte = base_de_partes.get(sn)

    if not parte:
        print("⚠️ No se encontró ninguna parte con ese número de serie.")
        return

    # Cálculo del promedio usando map y lambda
    promedio = sum(map(lambda x: x, parte["resultados_pruebas"])) / len(parte["resultados_pruebas"])
    parte["estado"] = "Aprobado" if promedio >= 90 else "Rechazado"

    print(f"✅ Evaluación completada. Estado actualizado a: {parte['estado']} ({promedio:.2f})")


def ver_inventario():
    # Muestra todas las piezas registradas
    if not base_de_partes:
        print("⚠️ No hay piezas registradas.")
        return

    print("\n--- Inventario Actual ---")
    for sn, datos in base_de_partes.items():
        print(f"S/N: {sn} - Tipo: {datos['tipo_componente']} - Estado: {datos['estado']}")


def contar_tipo(lista_partes, tipo):
    # Función recursiva para contar piezas de un tipo específico
    if not lista_partes:
        return 0
    primera, *resto = lista_partes
    return (1 if primera["tipo_componente"] == tipo else 0) + contar_tipo(resto, tipo)


def conteo():
    # Cuenta las piezas por tipo de componente
    if not base_de_partes:
        print("⚠️ No hay piezas registradas para contar.")
        return

    tipo = input(f"Ingrese el tipo de componente para contar {COMPONENTES_VALIDOS}: ").strip().capitalize()
    if tipo not in COMPONENTES_VALIDOS:
        print("⚠️ Tipo de componente no válido.")
        return

    total = contar_tipo(list(base_de_partes.values()), tipo)
    print(f"🔍 Total de piezas tipo '{tipo}': {total}")


#! Bucle Principal

print("--- Sistema de Control de Calidad ---")

while True:
    print("\n--- Menú Principal ---")
    print("1.- Registrar")
    print("2.- Buscar")
    print("3.- Evaluar")
    print("4.- Ver inventario")
    print("5.- Conteo")
    print("6.- Salir")

    opcion = input("Seleccione una opción: ").strip().lower()

    if opcion == "registrar" or opcion == "1":
        registrar_parte()
    elif opcion == "buscar" or opcion == "2":
        buscar_parte()
    elif opcion == "evaluar" or opcion == "3":
        evaluar_parte()
    elif opcion == "ver inventario" or opcion == "4":
        ver_inventario()
    elif opcion == "conteo" or opcion == "5":
        conteo()
    elif opcion == "salir" or opcion == "6":
        print("👋 Cerrando sistema de QC... ¡Hasta pronto!")
        break
    else:
        print("⚠️ Opción no válida, intenta de nuevo.")