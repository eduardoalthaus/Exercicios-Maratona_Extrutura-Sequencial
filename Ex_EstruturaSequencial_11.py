'''
11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    a - o produto do dobro do primeiro com metade do segundo .
    b - a soma do triplo do primeiro com o terceiro.
    c - o terceiro elevado ao cubo.
'''

n1 = input("Informe um numero inteiro: ")
n2 = input("Informe outro numero inteiro: ")
n3 = input("Informe um numero real: ")

a = (int(n1) * 2) + (float(n3) / 2)
b = (int(n1) * 3) + float(n3)
c = (float(n3) ** 3)

print("\nO produto do dobro do primeiro numero com a metade do segundo numero e:", a)
print("A soma do triplo do primeiro com o terceiro e:", b)
print("O terceiro numero elevado ao cubo e:", c)