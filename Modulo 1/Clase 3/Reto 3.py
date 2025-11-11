# Reto 3: Crear y manipular una lista de perfil de usuario

# Pide al usuario Nombre y Año de Nacimiento
nombre = (str(input("Escribe tu nombre: ")))
año = (int(input("Escribe tu año de nacimiento: ")))

# Pide al usuario sus 3 videojuegos favoritos
videojuegos = (str(input("Escribe el nombre de tus 3 videosjuegos favoritos separados por comas: ")))

# Lista "Perfil" que contenga el Nombre del Usuario
perfil = [nombre]

# Calcular edad
edad = 2025 - año

# Añadir edad a lista "Perfil"
perfil.append (edad)

# Tomar str videojuegos, convertir en lista y extender
lista_videojuegos = videojuegos.split(", ")
perfil.extend (lista_videojuegos)

# Insertar valor Booleano "True" al la lista 
perfil.insert(0, True)

# Quitar videojuego favorito
vj_favorito = perfil.pop(3)
print(f"Videojuego favorito: {vj_favorito}")
print(f"Perfil después de eliminar videojuego favorito: {perfil}")

# Comprobaciones Lógicas
mayor_edad = edad >= 18
nombre_largo = len(nombre) > 10
gamer_retro = 'Pacman' in perfil

# Imprimir Resultados Finales
print(f"Perfil: {perfil}")
print(f"Videojuego Favorito: {vj_favorito.capitalize()}")

print(f"El usuario es mayor de edad?: {mayor_edad}")
print(f"{nombre}, tu nombre es mayor a 10 caracteres?: {nombre_largo}")
print(f"{nombre}, eres un gamer retro?: {gamer_retro}")
