# 10. Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em
# consideração os anos bissextos).
from datetime import date

print("\n*** Dias entre as Datas ***\n")

print("--- Primeira data ---")
d1 = int(input("Dia: "))
m1 = int(input("Mês: "))
a1 = int(input("Ano: "))

print("\n--- Segunda data ---")
d2 = int(input("Dia: "))
m2 = int(input("Mês: "))
a2 = int(input("Ano: "))

data1 = date(a1, m1, d1)
data2 = date(a2, m2, d2)
dias = abs((data2 - data1).days)

print(f"\nQuantidade de dias entre as datas: {dias}")