'''
07 - Faça um programa que calcule a area de um quadrado, em seguida mostre o dobro desta area para o usuario
'''

lado = input("Informe o valor em metros ou centimetros do lado do quadrado: ")

area = int(lado) ** 2
d_area = area * 2

print("A area do quadrado e de: %.2f" % area, "metros ou centimetros quadrados, e o dobro e: %.2f" % d_area)