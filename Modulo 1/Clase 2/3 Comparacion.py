# Operadores de comparación y lógicos

x = 10
y = 20
print("Igualdad: ", x == y )
print("Desigualdad: ", x != y)
print("Mayor que: ", x > y )
print("Menor que: ", x < y )

#Lógicos

#!Recordemos: 
#! And 1*1 = 1, 1*0 = 0, 0*1 = 0, 0*0 = 0
#! Or  1+1 = 1, 1+0 = 1, 0+1 = 1, 0+0 = 0
#! Not 1 = 0, 0 = 1

p = True 
q = False
print("AND: ", p and q) #Ambos deben ser True
print("OR: ", p or q)   #Al menos uno debe ser True
print("NOT p: ", not p)  #Invierte el valor de p
print("NOT q: ", not q)  #Invierte el valor de q

a = int(input("Ingrese un valor para a: "))
b = int(input("Ingrese un valor para b: "))

print(f"La igualdad de {a} y {b} es: {a == b}")
print(f"La desigualdad de {a} y {b} es: {a != b}")
print(f"{a} es mayor que {b}: {a > b}")
print(f"{a} es menor que {b}: {a < b}")
print(f"{a} es mayor o igual que {b}: {a >= b}")
print(f"{a} es menor o igual que {b}: {a <= b}")
print(f"El And de {a} > 5 y {b} < 15 es: {(a > 5) and (b < 15)}")
print(f"El Or de {a} > 5 o {b} < 15 es: {(a > 5) or (b < 15)}")
print(f"El Not de {a} > 5 es: {not (a > 5)}")
