# importação de bibliotecas
import pandas as pd
from calculo_distancia import distancia_entre_cidades, dicionario_cidades, salvar_csv

# Criação de variáveis globais
cidades = list()
ufs = list()
latitudes_e_longitudes = dict()
distancias = list()

# Usuário digitará o nome do arquivo .CSV que deseja ler
arquivo_csv = str(input("Digite o nome do arquivo .CSV que deseja ler: "))

# Criação de um Dataframe a partir do .CSV digitado
df_cidades = pd.read_csv(arquivo_csv)

# Tranformação das colunas do dataframe em listas
cidades = list(df_cidades["CIDADE"])
ufs = list(df_cidades["UF"])

# Requisição a API Nominatim
print("\nObtendo Latitudes e Longitudes...")
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
    salvar_csv(distancias)

# Fim do programa
print("\nPrograma finalizado com sucesso :)")