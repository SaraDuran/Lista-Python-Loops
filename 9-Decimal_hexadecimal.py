# 9. Elaborar um programa em Python que converta um número decimal em hexadecimal,
# fazendo uso do método de divisões sucessivas.

print("\n*** Decimal em hexadecimal ***\n")

hex_chars = "0123456789ABCDEF"
num = int(input("Digite um número decimal inteiro >= 0: "))

if num == 0:
    print("Hexadecimal: 0")
else:
    hexa = ""
    n = num
    while n > 0:
        resto = n % 16
        hexa = hex_chars[resto] + hexa
        n //= 16
    print(f"Hexadecimal: {hexa}")