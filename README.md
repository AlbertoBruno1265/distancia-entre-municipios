# Calculadora de distância entre cidades
## Resumo
Uma aplicação simples que faz requisições a uma API para obter a latitude e a longitude de diversas cidades e calcular a ditância em linha reta entre elas
## Requisitos
- Python 3.6 >
- Pandas

# Funcionamento
O arquivo "calculo_distancia.py" contêm as funções: dicionario_cidades(), distancia_entre_cidades(), salvar_csv()

**distancia_entre_cidades(lista_cidades, lista_estados):** 
Recebe duas listas como parâmetro: *lista_cidades* e *lista_estados*.
Itera com um laço **for** sobre cada cidade e estado. 
Faz requisição na API **nominatim** e salva a latitude e longitude de cada cidade em um dicionário. No fim retorna esse dicionário.