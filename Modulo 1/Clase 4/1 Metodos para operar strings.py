
# Método para operar strings
cadena = input("Escribe una cadena de texto: ")

# Upper y Lower
print("La cadena en mayúsculas es:", cadena.upper()) # Convierte toda la cadena a mayúsculas
print("La cadena en minúsculas es:", cadena.lower()) # Convierte toda la cadena a minúsculas

# Capitalize
print("La cadena con la primera letra en mayúscula es:", cadena.capitalize()) # Convierte la primera letra de la cadena a mayúscula

# Title
print("La cadena con cada palabra en mayúscula es:", cadena.title()) # Convierte la primera letra de cada palabra a mayúscula

# Replace
print("La cadena con las vocales en mayúscula es:", cadena.replace('a', 'A').replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U'))

print("La cadena con las consonantes en mayúscula es:", ''.join([char.upper() if char.lower() not in 'aeiou' and char.isalpha() else char for char in cadena]))

# Strip
print("La cadena con espacios eliminados al inicio y al final es:", cadena.strip()) #Elimina los espacios al inicio y al final
print("La cadena con espacios eliminados al inicio es:", cadena.lstrip()) #Elimina los espacios al inicio
print("La cadena con espacios eliminados al final es:", cadena.rstrip()) #Elimina los espacios al final
print("La cadena eliminando todos los espacios es:", cadena.replace(" ", "")) #Elimina todos los espacios