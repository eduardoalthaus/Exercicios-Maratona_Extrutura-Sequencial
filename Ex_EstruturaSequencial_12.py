'''
12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''

altura = input("Informe sua altura separando os centimetros por '.': ")

peso_ideal = (72.7 * float(altura)) - 58

print("O seu peso ideal e: %.2f" % peso_ideal)