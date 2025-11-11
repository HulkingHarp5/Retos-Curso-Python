#Caculadora

a=int(input("Ingrese un valor para a: "))
b=int(input("Ingrese un valor para b: "))

print(f"Suma: {a+b}")
print(f"Resta: {a-b}")
print(f"multiplicación: {a*b}")
print(f"División: {a/b}")
print(f"División entera: {a//b}")
print(f"Módulo: {a%b}")
print(f"Potencia cúbica: {(a*b)**3}")

#Asignación

a=int(input("Ingrese un valor para a: "))
b=int(input("Ingrese un valor para b: "))

a += 2
print(f"Suma a +2: {a}")

a -= 13
print(f"Resta a -13: {a}")

b += 2
print(f"Suma b +2: {b}")

b-= 13
print(f"Resta b -13: {b}")

#Comparación

print(f"Igualdad a y b: {a==b}")
print(f"Desigualdad a y b: {a!=b}")
print(f"a mayor que b: {a>b}")
print(f"a menor que b: {a<b}")
print(f"a mayor o igual que b: {a>=b}")
print(f"a menor o igual que b: {a<=b}")

#Tabla de verdad AND sin valores de entrada
print(f"False AND False: {False and False}")
print(f"False AND True: {False and True}")
print(f"True AND False: {True and False}")
print(f"True AND True: {True and True}")

#Tabla de verdad OR sin valores de entrada
print(f"False OR False: {False or False}")
print(f"False OR True: {False or True}")
print(f"True OR False: {True or False}")
print(f"True OR True: {True or True}")

#Tabla de verdad NOT sin valores de entrada
print(f"NOT False: {not False}")
print(f"NOT True: {not True}")