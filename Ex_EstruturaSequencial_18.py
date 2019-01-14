'''
18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

mb = float(input("Informe o tamanho do arquivo para download em MB: "))
mbps = float(input("Informe a velocidade de download: "))

mbpm = mbps * 60
tempo_de_download = mb / mbpm

print("O download sera concluido em aproximadamente: %.2f" % tempo_de_download, "minutos!")