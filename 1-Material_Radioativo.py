# 1. Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
# Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
# para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa
# final e o tempo calculado em segundos.

print("\n*** MATERIAL RADIOATIVO ***\n")

massa = float(input("Massa inicial (em gramas): "))
tempo = 0

while massa >= 0.5:
    massa /= 2
    tempo += 50

print(f"Massa final: {massa:.4f} g")
print(f"Tempo necessário: {tempo} segundos")