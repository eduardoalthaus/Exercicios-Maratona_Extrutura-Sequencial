'''
08 - Faça um programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mes. Calcule e mostre o total do seu salario no referido mes.
'''

sal = input("Informe o quanto voce ganha por horas trabalhadas: ")
hr = input("Informe as horas trabalhadas no mes referido: ")

sal_mes = float(sal) * float(hr)

print("O salario a ser recebido no mes referido e de: %.2f" % sal_mes, "reais.")