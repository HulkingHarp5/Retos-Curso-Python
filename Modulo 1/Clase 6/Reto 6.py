# Reto 6:

# Lista Inicial
inventario_inicial = ["Halo, Abiotic Factor, Fortnite, For Honor, Grand Theft Auto V, Call of Duty, Minecraft"]
inventario = inventario_inicial[0].split(", ")
print(f"Inventario inicial: {inventario}")

# Menú de Opciones
while True:
    print("\n--- Menú Principal ---")
    print("1.- Añadir")
    print("2.- Quitar")
    print("3.- Ver")
    print("4.- Inspeccionar")
    print("5.- Salir")

    opcion = input("Seleccione una opción del menú: ").strip().lower() 
    # Opción Añadir
    if opcion == "añadir":
        nuevo_juego = input("Qué juego deseas añadir? ").strip()
        inventario.append(nuevo_juego)
        print("Nuevo juego añadido exitosamente al inventario!")
        print(f"Inventario actual: {inventario}")
    # Opción Quitar
    elif opcion == "quitar":
        juego_a_quitar = input("Qué juego deseas quitar? ").strip()
        if juego_a_quitar in inventario:
            inventario.remove(juego_a_quitar)
            print(f"{juego_a_quitar} se ha quitado exitosamente del inventario!")
        else:
            print(f"⚠️ El juego '{juego_a_quitar}' no se encuentra en el inventario.")
        print(f"Inventario actual: {inventario}")
    # Opción Ver
    elif opcion == "ver":
        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for i, juego in enumerate(inventario, start=1):
                print(f"{i}. {juego}")
    # Opción Inspeccionar
    elif opcion == "inspeccionar":
        if len(inventario) == 0:
            print("Inventario vacío.")
            continue

        while True:  # Bucle interno: no volvemos al menú hasta validar la inspección
            try:
                indice_str = input("Ingrese el número del juego que desea inspeccionar: ").strip()
                indice = int(indice_str) - 1   
                print(f"Has seleccionado el juego: {inventario[indice]}")
                break  # índice válido -> salimos del bucle interno y volvemos al menú principal
            except ValueError:
                print("⚠️ Error: Ingrese un número válido.")
                continue
            except IndexError:
                print(f"⚠️ Error: Número fuera de rango. Intenta con un número del 1 al {len(inventario)}.")
                continue
    # Opción Salir
    elif opcion == "salir":
        print("Saliendo del inventario.")
        break

    else:
        print("⚠️ Opción no válida. Por favor, seleccione una opción del menú.")
