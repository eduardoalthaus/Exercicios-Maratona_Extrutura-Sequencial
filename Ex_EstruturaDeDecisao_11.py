'''
11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
'''

sal = float(input("Informe o salario: "))

if sal <= 280.00:
    valsal = sal + (sal * 20 / 100)
elif sal >= 281.00 and sal <= 700.00:
    valsal = sal + (sal * 15 / 100)
elif sal >= 701.00 and sal <= 1500.00:
    valsal = sal + (sal * 10 / 100)
else:
    valsal = sal + (sal * 5 / 100)

print("Salario antes do reajuste: ", sal)
print("Percentual reajustado: %.1f" % (((valsal - sal) / sal) * 100))
print("Valor de aumento: %.1f" % (valsal - sal))
print("Novo salario: ", valsal)