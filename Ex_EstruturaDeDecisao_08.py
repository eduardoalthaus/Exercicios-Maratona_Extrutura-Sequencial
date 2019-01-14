'''
08 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''

p1 = input("Informe um produto: ")
v1 = float(input("Informe o valor deste produto: "))
p2 = input("Informe um produto: ")
v2 = float(input("Informe o valor deste produto: "))
p3 = input("Informe um produto: ")
v3 = float(input("Informe o valor deste produto: "))

print("\nOs produtos listados foram:", p1, ",", p2, "e", p3,"\n")

if v1 < v2 and v1 < v3:
    print("Com base no baixo custo, o produto indicado para compra seria a(o):", p1,".")
elif v2 < v1 and v2 < v3:
    print("Com base no baixo custo, o produto indicado para compra seria a(o):", p2,".")
elif v3 < v1 and v3 < v2:
    print("Com base no baixo custo, o produto indicado para compra seria a(o):", p3,".")