# Reto 7:

# Tupla de materias válidas
materias_validas = ("Programacion, Estructura de Datos, Algoritmos, Bases de Datos")

# Diccionario principal vacío
estudiantes = {}

print("--- Sistema de Administración de Estudiantes ---")

#MENÚ PRINCIPAL
while True:
    print("\n--- Menú Principal ---")
    print("1.- Registrar")
    print("2.- Buscar")
    print("3.- Promedio")
    print("4.- Ver todos")
    print("5.- Cursos unicos")
    print("6.- Salir")

    opcion = input("Seleccione una opción: ").strip().lower()

    #! Registrar estudiante
    if opcion == "registrar":

        # Pedir ID y Validar
        id_alumno = input("Ingrese el ID del alumno: ").strip()
        if id_alumno in estudiantes:
            print("⚠️ Error: Ese ID ya está registrado.")
            continue

        nombre = input("Ingrese el nombre del alumno: ").strip()

        # Validar materia
        print(f"Materias válidas: {materias_validas}")
        materia = input("Ingrese la materia: ").strip()
        if materia not in materias_validas:
            print("⚠️ Error: Materia no válida.")
            continue

        # Validar 3 calificaciones
        calificaciones = []
        for i in range(3):
            while True:
                try:
                    cal = float(input(f"Ingrese la calificación {i + 1}: "))
                    if cal < 0 or cal > 10:
                        print("⚠️ Ingrese un número entre 0 y 10.")
                        continue
                    calificaciones.append(cal)
                    break
                except ValueError:
                    print("⚠️ Error: Ingrese solo números válidos.")

        # Crear el diccionario anidado
        estudiantes[id_alumno] = {
            "nombre": nombre,
            "materia": materia,
            "calificaciones": calificaciones
        }

        print(f"✅ Alumno {nombre} registrado exitosamente.")

    #! Buscar estudiante
    elif opcion == "buscar":

        # Pedir ID y buscar
        id_alumno = input("Ingrese el ID del alumno a buscar: ").strip()
        if id_alumno in estudiantes:
            datos = estudiantes[id_alumno]
            print(f"Nombre: {datos['nombre']}")
            print(f"Materia: {datos['materia']}")
            print(f"Calificaciones: {datos['calificaciones']}")
        else:
            print("⚠️ No se encontró ningún alumno con ese ID.")
    #! Promedio
    elif opcion == "promedio":

        # Pedir ID y calcular promedio
        id_alumno = input("Ingrese el ID del alumno para calcular su promedio: ").strip()
        if id_alumno in estudiantes:
            calificaciones = estudiantes[id_alumno]["calificaciones"]
            promedio = sum(calificaciones) / len(calificaciones)
            print(f"Promedio de {estudiantes[id_alumno]['nombre']}: {promedio:.2f}")
        else:
            print("⚠️ No se encontró ningún alumno con ese ID.")
    #! Ver todos los estudiantes
    elif opcion == "ver todos":
        if len(estudiantes) == 0:
            print("⚠️ No hay estudiantes registrados.")
        else:
            print("Lista de estudiantes registrados:")
            for id_alumno, datos in estudiantes.items():
                print(f"ID: {id_alumno} | Nombre: {datos['nombre']} | Materia: {datos['materia']}")
    #! Cursos únicos
    elif opcion == "cursos unicos":
        # Set para mostrar materias sin repetir
        cursos = {datos["materia"] for datos in estudiantes.values()}
        if len(cursos) == 0:
            print("⚠️ No hay materias registradas aún.")
        else:
            print("Materias únicas registradas:")
            for c in cursos:
                print("-", c)
    #! Salir
    elif opcion == "salir":
        print("👋 Saliendo del sistema. ¡Hasta pronto!")
        break

    else:
        print("⚠️ Opción no válida, intenta de nuevo.")