'''
16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

m2 = float(input("Informe a quantidade de metros quadrados a ser pintado:"))

lata_tinta = 18
litros_necessarios = float(m2 / 3)
latas_usadas = litros_necessarios / lata_tinta
custo_lata_tinta = latas_usadas * 80

print("A quantidade necessaria de latas de tinta para cobrir a area informada e: %.2f" % latas_usadas, "latas")
print("O custo total das tintas e de: %.2f" % custo_lata_tinta, "reais")
