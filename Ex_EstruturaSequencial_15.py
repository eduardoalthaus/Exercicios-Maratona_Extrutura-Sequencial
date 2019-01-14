'''
15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
'''

def reducao_IR(sal_mes, ir):
    resultado = (sal_mes + (sal_mes * ir / 100))
    return round(sal_mes - resultado)


def reducao_INSS(sal_mes, inss):
    resultado = (sal_mes + (sal_mes * inss / 100))
    return round(sal_mes - resultado)


def reducao_SINDICATO(sal_mes, sind):
    resultado = (sal_mes + (sal_mes * sind / 100))
    return round(sal_mes - resultado)

sal = float(input("Informe o quanto voce ganha por horas trabalhadas: "))
hr = input("Informe as horas trabalhadas no mes referido: ")
ir = 11
inss = 8
sind = 5
sal_mes = float(sal) * float(hr)
val_ir = reducao_IR(sal_mes, ir)
val_inss = reducao_INSS(sal_mes, inss)
val_sind = reducao_SINDICATO(sal_mes, sind)
sal_liq = sal_mes + (val_ir + val_inss + val_sind)

print("O salario bruto a ser recebido no mes referido e de: %.2f" % sal_mes, "reais. No entanto, com descontos de\nimposto de renda, INSS e taxa sindical, o valor liquido a ser recebido e de: %.2f" % sal_liq, "reais.")
print("Valor de IR descontado:", val_ir * -1, "reais.")
print("Valor de INSS descontado:", val_inss * -1, "reais.")
print("Valor de taxa sindical descontado:", val_sind * -1, "reais.")