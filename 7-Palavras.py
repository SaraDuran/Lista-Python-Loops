# 7. Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
# parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
# conjunto de palavras.

print("\n*** Palavras com A ***\n")

total_a = 0

while True:
    palavra = input("Digite uma palavra (ou Enter vazio para sair): ").strip()
    if palavra == "":
        break
    for letra in palavra:
        if letra.lower() == "a":
            total_a += 1

print(f"Total de letras 'A' encontradas: {total_a}")