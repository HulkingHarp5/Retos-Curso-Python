# Reto 9:

# Estructura de Datos Inicial
TIPOS_ENTRADA_VALIDOS = ("Observación", "Prueba", "Error", "Mantenimiento")
ARCHIVO = "laboratorio.txt"

# Función para registrar una entrada
def registrar_entrada():
    print("\n--- Registrar nueva entrada ---")
    print("Tipos válidos:", ", ".join(TIPOS_ENTRADA_VALIDOS))

    # Validar tipo de entrada
    tipo = input("Ingrese el tipo de entrada: ").strip().capitalize()
    while tipo not in TIPOS_ENTRADA_VALIDOS:
        print("⚠️ Tipo no válido. Intente con uno de los siguientes:")
        print(", ".join(TIPOS_ENTRADA_VALIDOS))
        tipo = input("Ingrese el tipo de entrada: ").strip().capitalize()

    descripcion = input("Ingrese la descripción de la entrada: ").strip() # strip para evitar espacios en blanco

    # Guardar en el archivo sin borrar lo anterior (Me ayudó el buen Chat GPT)
    try:
        with open(ARCHIVO, "a", encoding="utf-8") as archivo: # encoding para evitar errores con caracteres especiales
            archivo.write(f"TIPO: {tipo} - DESCRIPCIÓN: {descripcion}\n")
        print("✅ Entrada registrada correctamente.")
    except Exception as e:
        print(f"❌ Error al guardar la entrada: {e}")

# Función para ver el registro completo
def ver_log():
    print("\n--- Registro de Laboratorio ---")
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo: 
            contenido = archivo.read()
            if contenido.strip() == "": 
                print("El log está vacío.")
            else:
                print(contenido)
    except FileNotFoundError:
        print("⚠️ El log está vacío o no se ha creado todavía.")
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")

# Función Principal
def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar")
        print("2. Ver log")
        print("3. Salir")

        opcion = input("Seleccione una opción del menú: ").strip().lower()

        if opcion == "1" or opcion == "registrar":
            registrar_entrada()
        elif opcion == "2" or opcion == "ver_log":
            ver_log()
        elif opcion == "3" or opcion == "salir":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")

# Ejecución del programa
if __name__ == "__main__":
    main() # Esto hace que el programa inicie llamando a la función main
