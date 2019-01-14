'''
14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

peso_de_peixes = float(input("Informe o peso total dos peixes pescados do dia: "))
limite_peso_peixes = 50
peso_rest = limite_peso_peixes - peso_de_peixes
excedente =  peso_de_peixes - limite_peso_peixes
multa = excedente * 4.0

if peso_de_peixes < limite_peso_peixes:
    print("Limite diario de peso nao excedido! Peso restante para atingir o limite: %.2f" % peso_rest)
elif peso_de_peixes == limite_peso_peixes:
    print("Limite diario de peso atingido!")
elif peso_de_peixes > limite_peso_peixes:
        excedente
        print("Limite diario de peso excedido em: %.2f" % excedente, "quilos! Havera multa de: %.2f" % multa, "reais!")
