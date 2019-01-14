'''
06 - Fala um programa que peça o raio de um circulo, calcule e mostre sua area.
'''

raio = input("Informe o RAIO (em centimetros ou metros) para que se calcule a area: ")
pi = 3.14
area_circulo = int(raio) ** 2 * pi

print("A area do circulo e de: %.2f" % area_circulo, "metros ou centimetros quadrados!")