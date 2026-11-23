# 6. Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
# primeiro e último nome.

print("\n*** Pedra, papel e tesoura ***\n")

nome_completo = input("Digite seu nome completo: ").strip()
partes = nome_completo.split()

if len(partes) >= 2:
    print(f"Primeiro nome: {partes[0]}")
    print(f"Último nome: {partes[-1]}")
elif len(partes) == 1:
    print(f"Apenas um nome informado: {partes[0]}")
else:
    print("Nenhum nome digitado.")