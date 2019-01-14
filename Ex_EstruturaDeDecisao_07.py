'''
07 - Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

n1 = float(input("Informe o numero 1: "))
n2 = float(input("Informe o numero 2: "))
n3 = float(input("Informe o numero 3: "))

if n1 > n2 and n1 > n3:
    print("O numero", n1, "e o maior!")
elif n2 > n1 and n2 > n3:
    print("O numero", n2, "e o maior!")
elif n3 > n1 and n3 > n2:
    print("O numero", n3, "e o maior!")

if n1 < n2 and n1 < n3:
    print("O numero", n1, "e o menor!")
elif n2 < n1 and n2 < n3:
    print("O numero", n2, "e o menor!")
elif n3 < n1 and n3 < n2:
    print("O numero", n3, "e o menor!")
