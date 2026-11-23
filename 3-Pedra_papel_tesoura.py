# 3. Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
# porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.

print("\n*** Pedra, papel e tesoura ***\n")

opcoes = ["pedra", "papel", "tesoura"]
pontos_vitoria = int(input("Quantos pontos para vencer? "))
p1 = p2 = 0

while p1 < pontos_vitoria and p2 < pontos_vitoria:
    j1 = input("\nJogador 1 (pedra/papel/tesoura): ").strip().lower()
    j2 = input("Jogador 2 (pedra/papel/tesoura): ").strip().lower()

    if j1 not in opcoes or j2 not in opcoes:
        print("Jogada inválida! Tente novamente.")
        continue

    if j1 == j2:
        print("Empate!")
    elif (
        (j1 == "pedra" and j2 == "tesoura")
        or (j1 == "tesoura" and j2 == "papel")
        or (j1 == "papel" and j2 == "pedra")
    ):
        p1 += 1
        print(f"Ponto do Jogador 1! Placar: {p1} x {p2}")
    else:
        p2 += 1
        print(f"Ponto do Jogador 2! Placar: {p1} x {p2}")

vencedor = "Jogador 1" if p1 == pontos_vitoria else "Jogador 2"
print(f"\n🏆 {vencedor} venceu!")