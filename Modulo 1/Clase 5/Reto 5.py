
# Reto 5

# Solicitamos la cantidad de alumnos a registrar
total_alumnos = int(input("Ingrese la cantidad de alumnos que va a registrar: "))

# Listas para almacenar nombres y calificaciones
nombres = []
calificaciones = []

# Listas para clasificar alumnos
aprobados = []
reprobados = []
excelentes = []

# Variables
suma_total = 0.0
calif_min = 0.0 
calif_max = 0.0

# Registro de alumnos
for i in range(total_alumnos):
    print(f"Alumno {i + 1}: ")
    
    nombre = input("Nombre del alumno: ")
    calif = float(input(f"Calificación de {nombre}: "))
    nombres.append(nombre)
    calificaciones.append(calif)
    
    suma_total = suma_total + calif
    
    if calif == 10:
        excelentes.append(nombre)
    elif calif >= 6:
        aprobados.append(nombre)
    elif calif < 6:
        reprobados.append(nombre)
    
    # Si es el primer alumno (i == 0), su calificación es la min y max temporal
    if i == 0:   # ----> Me ayudó chatGPT con esta parte <----
        calif_min = calif
        calif_max = calif
    else:
        # Si la calificación actual es menor que la mínima guardada, la reemplazamos
        if calif < calif_min:
            calif_min = calif
        # Si la calificación actual es mayor que la máxima guardada, la reemplazamos
        if calif > calif_max:
            calif_max = calif

# Calculamos promedio
promedio = suma_total / total_alumnos


# Listas de resultados
print("Listas de Resultados:")
print(f"Número total de estudiantes: {total_alumnos}")
print(f"Promedio general del salón: {promedio}")
print(f"Calificación más alta: {calif_max}")
print(f"Calificación más baja: {calif_min}")

# Clasificación de alumnos
print("Clasificación de alumnos:")
print(f"Alumnos Excelentes: {excelentes}")
print(f"Alumnos Aprobados: {aprobados}")
print(f"Alumnos Reprobados: {reprobados}")