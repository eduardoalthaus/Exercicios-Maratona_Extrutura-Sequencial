'''
04 - Faça um programa que peça as 4 notas bimestrais e mostre a media.
'''

Titulo = ("Gerador de media Bimestral")
print(Titulo)

mat = input("informe a nota de mat:")
geo = input("informe a nota de geo:")
his = input("informe a nota de his:")
por = input("informe a nota de por:")
bio = input("informe a nota de bio:")
soc = input("informe a nota de soc:")
fil = input("informe a nota de fil:")

media =  (int(mat) + int(geo) + int(his) + int(por) + int(bio) + int(soc) + int(fil)) / 7

print("A media a sua media Bimestral e:", int(media))