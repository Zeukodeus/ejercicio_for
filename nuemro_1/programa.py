n = int(input("Ingrese la cantidad de números a leer: "))

pares = 0
impares = 0

for i in range(n):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Se leyeron", pares, "números pares y", impares, "números impares.")
