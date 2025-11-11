
# Diccionarios
# Son estructuras de datos que almacenan pares de clave-valor.
# Se definen utilizando llaves {}

print("-"*3)
persona = {"nombre": "Ana", "edad": 20, "altura": 1.65}

# Podemos acceder a los valores mediante sus claves
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Altura:", persona["altura"])

#? De igual manera, podemos modificar los valores asociados a una clave
persona["edad"] = 21
print("Edad actualizada:", persona["edad"])
#? Añadir nuevos pares clave-valor, simplemente asignando un valor a una nueva clave
persona["ciudad"] = "México"
print("Ciudad añadida:", persona["ciudad"])
persona["Color favorito"] = input("¿Cuál es tu color favorito?: ")
print("Color favorito añadido:", persona["Color favorito"]) 