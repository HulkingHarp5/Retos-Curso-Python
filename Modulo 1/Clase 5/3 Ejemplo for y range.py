
for numero in range (1,11):
    print(f"El número es: {numero}")

materiales_pruepa_split = ["acero, madera, pástico"]
materiales = materiales_pruepa_split[0].split(", ")
print(f"Divición .split de lista materiales: {materiales}")
for material in materiales:
    print(f"El material es: {material.capitalize()}")