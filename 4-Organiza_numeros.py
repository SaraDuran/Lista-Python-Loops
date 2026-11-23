# 4. Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
# crescente.
print("\n*** 5 números ***\n")

numeros = []
for i in range(5):
    numeros.append(float(input(f"Digite o {i + 1}º número: ")))

for i in range(len(numeros)):
    for j in range(0, len(numeros) - 1 - i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Ordem crescente:", numeros)