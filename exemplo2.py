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

