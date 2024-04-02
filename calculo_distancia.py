def dicionario_cidades(lista_cidades, lista_estados):
    import requests

    dic_cidade = dict()

    for i in range(0, len(lista_cidades)):

        cidade = lista_cidades[i].replace(" ", "+")

        request = f'''http://nominatim.openstreetmap.org/search?city={cidade}&state={lista_estados[i]}&country=Brazil&format=json'''

        response = requests.get(request).json()

        chave = f"{lista_cidades[i]} - {lista_estados[i]}"

        lat = float(response[0]["lat"])
        lon = float(response[0]["lon"])

        dic_cidade[chave] = [lat, lon]

    return dic_cidade

def distancia_entre_cidades(dic, chv1, chv2):
    from math import sqrt

    deltaLat = dic[chv1][0] - dic[chv2][0]
    deltaLon = dic[chv1][1] - dic[chv2][1]

    distance = int(round(sqrt(deltaLat**2 + deltaLon**2) * 111110, 0))

    return distance
