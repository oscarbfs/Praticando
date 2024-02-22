import pandas as pd
from data.dados import Dados
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import numpy as np


resultados = pd.DataFrame(Dados.resultados)

# Obtendo informações do último sorteio no CSV
ultimo_sorteio_info = resultados.iloc[-1][['Data Sorteio', 'Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15']]

# Imprimindo o resultado previsto junto com as informações do último sorteio no CSV e a acurácia do modelo
print("Data do último sorteio:", ultimo_sorteio_info['Data Sorteio'])
print("Resultado do último sorteio:")
print(ultimo_sorteio_info[['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15']])
for i in range(10):
    
    print("\n")
    print("Previsao ", i+1)

    # Removendo colunas irrelevantes e separando as variáveis entre preditoras e variável alvo
    y = resultados[['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15']].shift(-1)[:-1] # variável alvo (os próximos números do sorteio)
    x = resultados.drop(['Concurso', 'Data Sorteio', 'Ganhadores 15 acertos', 'Cidade / UF', 'Rateio 15 acertos', 'Ganhadores 14 acertos', 'Rateio 14 acertos', 'Ganhadores 13 acertos', 'Rateio 13 acertos', 'Ganhadores 12 acertos', 'Rateio 12 acertos', 'Ganhadores 11 acertos', 'Rateio 11 acertos', 'Acumulado 15 acertos', 'Arrecadacao Total', 'Estimativa Prêmio', 'Acumulado sorteio especial Lotofácil da Independência', 'Observação'], axis=1)[:-1] # variáveis preditoras (removendo a última linha que não possui y correspondente)

    # Dividindo os dados em conjuntos de treinamento e teste
    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.50, random_state=42)

    # Criando modelo
    modelo = ExtraTreesRegressor()
    modelo.fit(x_treino, y_treino)

    # Prevendo dados de teste
    y_pred = modelo.predict(x_teste)

    # Calculando a acurácia do modelo
    acuracia = r2_score(y_teste, y_pred)

    # Removendo a coluna 'Data Sorteio' do último sorteio para a previsão
    ultimo_sorteio = ultimo_sorteio_info.drop('Data Sorteio') 

    # Prevendo próximo sorteio
    proximo_sorteio = modelo.predict(ultimo_sorteio.values.reshape(1, -1))

    # Convertendo os valores previstos para inteiros
    proximo_sorteio_int_baixo = proximo_sorteio.astype(int)
    proximo_sorteio_int_cima = np.ceil(proximo_sorteio).astype(int)
    proximo_sorteio_int_round = np.round(proximo_sorteio)

    print("\nAcurácia do modelo (R²):", acuracia)
    print("Próximo sorteio previsto (int pra baixo):", proximo_sorteio_int_baixo)
    print("Próximo sorteio previsto (int pra cima):", proximo_sorteio_int_cima)
    print("Próximo sorteio previsto (int round):", proximo_sorteio_int_round)
    print("Próximo sorteio previsto (float):", proximo_sorteio)


# 1  2  4  5  7  9 10 11 14 15 16 17 19 22 25  

# 1  2  3  5  7  8  9 11 13 14 16 17 19 22 24
# 2  3  4  6  8  9 10 12 14 15 17 18 20 23 25
# 1  2  4  5  7  9 10 11 14 15 16 17 19 22 25