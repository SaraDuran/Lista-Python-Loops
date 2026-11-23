# 8. Elaborar um programa que receba um número em binário, e mostre o seu valor em
# decimal.

print("\n*** Binario a Decimal ***\n")

binario = input("Digite um número binário: ").strip()
decimal = 0
potencia = len(binario) - 1

for digito in binario:
    if digito not in ("0", "1"):
        print("Entrada inválida! Use apenas 0 e 1.")
        decimal = None
        break
    decimal += int(digito) * (2 ** potencia)
    potencia -= 1

if decimal is not None:
    print(f"Valor em decimal: {decimal}")