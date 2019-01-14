'''
17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os         valores para cima, isto é, considere latas cheias.
'''

m2 = float(input("Informe a quantidade de metros quadrados a ser pintado:"))

litros_necessarios = float(m2 / 6) * 1.1 # 10% de folga
lata_tinta = int( litros_necessarios / 18)
galao_tinta = int(litros_necessarios / 3.6)

# Calculo de latas
if (litros_necessarios % 18 != 0):
    lata_tinta += 1

# Calculo de galoes
if (litros_necessarios % 3.6 != 0):
    galao_tinta += 1

# Calculo misturando latas e galoes
mixLatas = int(litros_necessarios / 18)
mixGaloes = int((litros_necessarios - (mixLatas * 18.0)) / 3.6)
if ((litros_necessarios - (mixLatas * 18.0) % 3.6 != 0)):
    mixGaloes += 1

print('Latas:', lata_tinta, '. Valor:', lata_tinta * 80)
print('Galoes', galao_tinta, '. Valor:', galao_tinta * 25)
print('Latas', mixLatas, 'e Galoes', mixGaloes, '. Valor: ', (mixLatas * 80)+(mixGaloes * 25))