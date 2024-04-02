def dicionario_cidades(lista_cidades, lista_estados):
    # Importação da biblioteca de requisição
    import requests

    # Criação do dicionário que gravará os dados
    dic_cidade = dict()

    for i in range(0, len(lista_cidades)):

        # Transformação do nome da cidade que fique adequada ao link de requisição
        cidade = lista_cidades[i].replace(" ", "+")

        # Construção do link de requesição
        request = f'''http://nominatim.openstreetmap.org/search?city={cidade}&state={lista_estados[i]}&country=Brazil&format=json'''

        # Captura da resposta da API
        response = requests.get(request).json()

        # Criação da chave do dicionário
        chave = f"{lista_cidades[i]} - {lista_estados[i]}"

        # Dados de Latitude e Longitude obtidos pela resposta da API
        lat = float(response[0]["lat"])
        lon = float(response[0]["lon"])

        # Dados salvos no dicionário
        dic_cidade[chave] = [lat, lon]

    # Retorna o dicionário com os dados
    return dic_cidade

def distancia_entre_cidades(dic, chv1, chv2):
    # Importação do método de raiz quadrada da biblioteca "math"
    from math import sqrt

    # Conculo da diferença entre Latitudes e Longitudes
    deltaLat = dic[chv1][0] - dic[chv2][0]
    deltaLon = dic[chv1][1] - dic[chv2][1]

    # Uso do teorema de pitágora para cálculo da distancia em linha reta (resultado em metros)
    # OBS.: Cada grau de uma latitude ou longitude equivale a 111110 metros.
    distancia = int(round(sqrt(deltaLat**2 + deltaLon**2) * 111110, 0))

    # Retorno da distância
    return distancia

def salvar_csv(cidades_e_distancias):
    # Lê o nome que o usuário deseja salvar
    nome_arquivo = input("Digite o nome do arquivo: ").lower()

    # Caso o usuário tenha esquecido a extensão, o programa adiciona
    if nome_arquivo.find(".csv") == -1:
        nome_arquivo += ".csv"
    
    # Cria ou dá um TRUNCATE no arquivo digitado
    with open(nome_arquivo, 'w') as arq:
        # Adiciona o cabeçalho ao arquivo
        arq.write("CIDADE1,CIDADE2,DISTANCIA\n")

        # Adiciona linhas ao arquivo
        for i in range(0, len(cidades_e_distancias)):
            arq.write(f"{cidades_e_distancias[i][0]},{cidades_e_distancias[i][1]},{cidades_e_distancias[i][2]}\n")
    
    # Encerra a função
    print("Arquivo salvo com sucesso!")