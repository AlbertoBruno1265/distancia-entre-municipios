# importação de bibliotecas
from os import system
from calculo_distancia import distancia_entre_cidades, dicionario_cidades, salvar_csv, ler_csv

# Limpa a tela do console
system("CLS")

# Criação de variáveis globais
latitudes_e_longitudes = dict()
distancias = list()

# Usuário digitará o nome do arquivo .CSV que deseja ler
arquivo_csv = str(input("Digite o caminho do arquivo .CSV que deseja ler: "))

# Leitura das cidades a partir do .CSV digitado
cidades_e_ufs =  ler_csv(arquivo_csv)

# Requisição a API Nominatim
print("\nObtendo Latitudes e Longitudes...")
latitudes_e_longitudes = dicionario_cidades(cidades_e_ufs[0], cidades_e_ufs[1])
print()

# Calculo das distancias dado as coordenadas
for i in range(0, len(cidades_e_ufs[0])):
    chave1 = f"{cidades_e_ufs[0][i]} - {cidades_e_ufs[1][i]}"

    for j in range(i+1, len(cidades_e_ufs[0])):
        chave2 = f"{cidades_e_ufs[0][j]} - {cidades_e_ufs[1][j]}"

        distancia = distancia_entre_cidades(latitudes_e_longitudes, chave1, chave2)

        distancias.append([chave1, chave2, distancia])

        print(f"{chave1}\t{chave2}\t{distancia}")

# Escolha caso queira gravar os dados em um arquivo CSV
resp = str(input("\nDeseja salvar estes dados em um CSV? [S/N]: ")).lower()

if resp == 's':
    salvar_csv(distancias)

# Fim do programa
print("\nPrograma finalizado com sucesso :)")