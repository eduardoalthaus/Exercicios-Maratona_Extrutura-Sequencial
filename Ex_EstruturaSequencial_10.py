'''
10 - Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
'''

gra_cel = input("Informe os graus em CELSIUS para conversao em FARENHEIT: ")

gra_far = (float(gra_cel) * 9/5) + 32

print(gra_cel, "graus Farenheit equivalem a: %.2f" % gra_far, "graus Celsius")