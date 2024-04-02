from os import system
from calculo_distancia import distancia_entre_cidades, dicionario_cidades

cidades = list()
ufs = list()
latitudes_e_longitudes = dict()
distancias = list()

num_cidades = int(input("Digite a quantidade de cidades que serão digitadas: "))

for i in range(0, num_cidades):
    system("CLS")
    cidades.append(str(input(f"Digite o nome da {i+1}ª cidade: ").upper()))
    ufs.append(str(input("Digite a Unidade Federativa: ").upper()))


latitudes_e_longitudes = dicionario_cidades(cidades, ufs)

for i in range(0, num_cidades):
    chave1 = f"{cidades[i] - ufs[i]}"

    for j in range(0, num_cidades):
        chave2 = f"{cidades[j] - ufs[j]}"

        distancia = distancia_entre_cidades(latitudes_e_longitudes, chave1, chave2)

        distancias.append([chave1, chave2, distancia])