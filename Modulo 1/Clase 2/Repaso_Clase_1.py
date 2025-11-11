#Input siempre devuelve un string
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
frase = input("Ingresa tu frase favorita: ")
dinero = float(input("Ingrese la cantidad de dinero que tiene: "))

print("Nombre: " + nombre)
print("Edad: " + str(edad) + " años")
print("Frase favorita: " + frase)
print("Dinero: $" + str(dinero))

#Concatenacion
print(f"Hola {nombre}, tienes {edad} años, tu frase favorita es '{frase}' y tienes ${dinero} en tu cuenta.")

#Otra forma de concatenar
print("Hola {}, tienes {} años, tu frase favorita es '{}' y tienes ${} en tu cuenta.".format(nombre, edad, frase, dinero))

#Otra forma de concatenar
print("Hola %s, tienes %d años, tu frase favorita es '%s' y tienes $%.2f en tu cuenta." % (nombre, edad, frase, dinero))

#Otra forma de concatenar
print("Hola " + nombre + ", tienes " + str(edad) + " años, tu frase favorita es '" + frase + "' y tienes $" + str(dinero) + " en tu cuenta.")