# 5. Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano,
# e um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever
# um programa em Python que seja capaz de calcular e iterativamente e no fim imprimir o
# tempo necessário para que a população do país A ultrapasse a população do país B

print("\n*** Taxa de natalidade ***\n")

pop_a = 5_000_000
pop_b = 7_000_000
anos = 0

while pop_a <= pop_b:
    pop_a *= 1.03
    pop_b *= 1.02
    anos += 1

print(f"Serão necessários {anos} anos para A ultrapassar B.")
print(f"População A: {int(pop_a)} | População B: {int(pop_b)}")