'''
02 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

n = float(input("Informe um valor, seja positivo ou negativo, caso negativo, informe o sinal a frente: "))

if n < 0:
    print("O numero informado e NEGATIVO!")
if n == 0:
    print("O numero informado e ZERO!")
elif n > 0:
    print("O numero informado e POSITIVO!")