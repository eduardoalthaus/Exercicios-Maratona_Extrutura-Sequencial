'''
04 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

l = input("Informe uma letra para saber se ela e vogal ou consoante: ")

a = 'a'
A = 'A'
e = 'e'
E = 'E'
i = 'i'
I = 'I'
o = 'o'
O = 'O'
u = 'u'
U = 'U'

if l == a or l == A or l == e or l == E or l == i or l == I or l == o or l == O or l == u or l == U:
    print("A letra informada e uma vogal!")
else:
    print("A letra informada e uma consoante!")