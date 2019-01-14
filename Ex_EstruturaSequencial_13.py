'''
13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
'''

altura = input("Informe sua altura separando os centimetros por '.': ")

peso_idealH = (72.7 * float(altura)) - 58
peso_idealM = 62.1 * float(altura) - 44.7
print("O peso ideal para homem e: %.2f" % peso_idealH, "e para mulher e: %.2f" % peso_idealM)