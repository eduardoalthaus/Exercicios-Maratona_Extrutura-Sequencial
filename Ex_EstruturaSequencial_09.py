'''
Fala um programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
'''

gra_far = input("Informe os graus em FARENHEIT para conversao em CELSIUS: ")

gra_cel = (float(gra_far) - 32) * 5/9

print(gra_far, "graus Farenheit equivalem a: %.2f" % gra_cel, "graus Celsius")