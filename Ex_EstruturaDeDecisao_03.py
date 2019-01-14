'''
03 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

l1 = input("Informe a letra que defina seu genero: ")

mulher = 'M'
homem = 'H'
mulher_trans = 'MT'
homem_trans = 'HT'
travesti = 'T'
androginia = 'A'
agenero = 'AG'
binarismo_de_genero = 'BG'
crossdresser = 'CD'
dragqueen = 'DQ'
dragking = 'DK'
genero_fluido = 'GF'
transformista = 'TF'
transgenero = 'TG'

if (l1 != 'M') and (l1 != 'H') and (l1 != 'MT') and (l1 != 'HT') and (l1 != 'T') and (l1 != 'A') and (l1 != 'AG') and (l1 != 'BG') and (l1 != 'CD') and (l1 != 'DQ') and (l1 != 'DK') and (l1 != 'GF') and (l1 != 'TF') and (l1 != 'TG'):
    print("Genero ainda nao cadastrado ou invalido!")
elif l1 == mulher:
    print("Genero MULHER informado!")
elif l1 == homem:
    print("Genero HOMEM informado!")
elif l1 == mulher_trans:
    print("Genero MULHER TRANS informado!")
elif l1 == homem_trans:
    print("Genero HOMEM TRANS informado!")
elif l1 == travesti:
    print("Genero TRAVESTI informado!")
elif l1 == androginia:
    print("Genero ANDROGENO informado!")
elif l1 == agenero:
    print("Genero AGENERO informado!")
elif l1 == binarismo_de_genero:
    print("Genero GENERO BINARIO informado!")
elif l1 == crossdresser:
    print("Genero CROSS DRESSER informado!")
elif l1 == dragqueen:
    print("Genero DRAG QUEEN informado!")
elif l1 == dragking:
    print("Genero DRAG KING informado!")
elif l1 == genero_fluido:
    print("Genero GENERO FLUIDO informado!")
elif l1 == transformista:
    print("Genero TRANSFORMISTA informado!")
elif l1 == transgenero:
    print("Genero TRANSGENERO informado!")