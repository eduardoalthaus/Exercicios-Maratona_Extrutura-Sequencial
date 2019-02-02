'''
09 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

n1 = input("Informe o primeiro numero: ")
n2 = input("Informe o segundo numero: ")
n3 = input("Informe o terceiro numero: ")

lista = [n1, n2, n3]

print(sorted(lista, key=int, reverse=True))