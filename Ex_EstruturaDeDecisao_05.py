'''
05 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

np1 = float(input("Informe uma nota parcial para calculo da media: "))
np2 = float(input("Informe outra nota parcial para calculo da media: "))

media = float((np1 + np2) / 2)

if media >= 70 and media <= 99:
    print("Aprovado!")
if media < 70:
    print("Reprovado!")
elif media == 100:
    print("Aprovado com Distinçao!")