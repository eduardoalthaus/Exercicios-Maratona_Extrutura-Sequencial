'''
03 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

l1 = input("Informe a letra que defina seu genero: ")

if l1 == 'M':
    print ("Genero Mulher informado!")
elif l1 == 'H':
    print ("Genero Homem  informado!")
elif l1 == 'MT':
    print ("Genero Mulher Trans informado!")
elif l1 == 'HT':
    print ("Genero Homem Trans informado!")
elif l1 == 'T':
    print ("Genero Travesti informado!")
elif l1 == 'A':
    print ("Genero Androginia informado!")
elif l1 == 'AG':
    print ("Genero Agenero informado!")
elif l1 == 'BG':
    print ("Genero Binarismo De Genero informado!")
elif l1 == 'CD':
    print ("Genero Crossdresser informado!")
elif l1 == 'DQ':
    print ("Genero Dragqueen informado!")
elif l1 == 'DK':
    print ("Genero Dragking informado!")
elif l1 == 'GF':
    print ("Genero Genero Fluido informado!")
elif l1 == 'TF':
    print ("Genero Transformista informado!")
elif l1 == 'TG':
    print ("Genero Transgenero informado!")
else:
    print ("Genero ainda nao cadastrado ou invalido!")
