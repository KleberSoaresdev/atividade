numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

impares = []
pares = []
positivos = []
negativos = []
zeros = []

for numero in numeros:
    if numero % 2 == 1:
        impares.append(numero)
    elif numero % 2 == 0:
        pares.append(numero)

    if numero > 0:
        positivos.append(numero)
    elif numero < 0:
        negativos.append(numero)
    else:
        zeros.append(numero)

print("Números ímpares:", impares)
print("Números pares:", pares)
print("Números positivos:", positivos)
print("Números negativos:", negativos)
print("Zeros:", zeros)
