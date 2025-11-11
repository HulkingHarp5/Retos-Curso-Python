lista1 = ["Leche, Pan, Huevos, Frutas, Verduras"]
lista_compras = lista1[0].split(", ")
print(f"Lista de compras: ",lista_compras)

print("--- MENÚ ---")
print("1.- Añadir")
print("2.- Quitar")
print("3.- Revisar")

opcion = str(input("Seleccione una opción del menú..."))
if opcion.lower() == "añadir":
    articulo_nuevo = (str(input("Qué artículo desea añadir a la lista? ")))
    lista_compras.append (articulo_nuevo)
    print(f"{articulo_nuevo} se ha añadido exitosamente a tu lista de compras! \n{lista_compras}")
elif opcion.lower() == "quitar":
    articulo_a_quitar = input("Qué producto desea eliminar? ")
    lista_compras.remove(articulo_a_quitar)
    print(f"{articulo_a_quitar} se ha eliminado exitosamente de tu lista de compras! \n{lista_compras}")
elif opcion.lower() == "revisar":
    print(f"Su lista de compras es: {lista_compras}")
