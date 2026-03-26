print("Inicio do Desafio 2:")

import statistics

empresa1 = [1000,6000,1200,8000,1400]

empresa2 = [5000,4000,3000,2000,7000]

empresa3 = [1200,1300,8000,3000,15000]

empresa4 = [1400,1750,2000,4500,5900]

def maior_media_max():
    media1 = statistics.mean (empresa1)
    media2 = statistics.mean (empresa2)
    media3 = statistics.mean (empresa3)
    media4 = statistics.mean (empresa4)

    print("Média Salarial da Empresa 1 R$:",media1)
    print("Média Salarial da Empresa 2 R$:",media2)
    print("Média Salarial da Empresa 3 R$:",media3)
    print("Média Salarial da Empresa 4 R$:",media4)


    mediana1 = statistics.stdev (empresa1)
    mediana2 = statistics.stdev(empresa2)
    mediana3 = statistics.stdev (empresa3)
    mediana4 = statistics.stdev (empresa4)

    print("A mediana da Empresa 1 é de: R$",mediana1)
    print("A mediana da Empresa 2 é de: R$",mediana2)
    print("A mediana da Empresa 3 é de: R$",mediana3)
    print("A mediana da Empresa 4 é de: R$",mediana4)

    media_salarial = [media1,media2,media3,media4]
    maior_media = max (media_salarial)
        
    print("A melhor opção é a Empresa 3, com maior média salarial, tendo o valor de: R$", maior_media)
maior_media_max ()