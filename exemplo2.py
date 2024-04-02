# importação de bibliotecas
import pandas as pd
from calculo_distancia import distancia_entre_cidades, dicionario_cidades

# Criação de variáveis globais
cidades = list()
ufs = list()
latitudes_e_longitudes = dict()
distancias = list()

df_cidades = pd.read_csv("exemplo.csv")

cidades = list(df_cidades["CIDADE"])
ufs = list(df_cidades["UF"])

print("Obtendo Latitudes e Longitudes...")
latitudes_e_longitudes = dicionario_cidades(cidades, ufs)
print()

# Calculo das distancias dado as coordenadas
for i in range(0, len(cidades)):
    chave1 = f"{cidades[i]} - {ufs[i]}"

    for j in range(i+1, len(cidades)):
        chave2 = f"{cidades[j]} - {ufs[j]}"

        distancia = distancia_entre_cidades(latitudes_e_longitudes, chave1, chave2)

        distancias.append([chave1, chave2, distancia])

        print(f"{chave1}\t{chave2}\t{distancia}")

# Escolha caso queira gravar os dados em um arquivo CSV
resp = str(input("\nDeseja salvar estes dados em um CSV? [S/N]: ")).lower()

if resp == 's':
    nome_arquivo = input("Digite o nome do arquivo: ").lower()

    if nome_arquivo.find(".csv") == -1:
        nome_arquivo += ".csv"
    
    with open(nome_arquivo, 'w') as arq:
        arq.write("cidade1,cidade2,distancia\n")

        for i in range(0, len(distancias)):
            arq.write(f"{distancias[i][0]},{distancias[i][1]},{distancias[i][2]}\n")
    
    print("Arquivo salvo com sucesso!")

# Fim do programa
print("\nPrograma finalizado com sucesso :)")