import matplotlib.pyplot as plt
import pandas as pd
from Dados.dados import Dados
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

vinhos = pd.DataFrame(Dados.vinhos)

print(vinhos.head())

vinhos['style'] = vinhos['style'].replace('red', 0)
vinhos['style'] = vinhos['style'].replace('white', 1)

# Separando as variaveis entre preditoras e variavel alvo
y = vinhos['style'] # variavel alvo
x = vinhos.drop('style', axis = 1) # variaveis preditoras

# Criando os cojuntos de dados de treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Criando modelo
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

# Imprimindo resultados
resultado = modelo.score(x_teste, y_teste)
print("Acuária: ", resultado)

print(y_teste[400:403])
print(x_teste[400:403])

# Prevendo dados
print(modelo.predict(x_teste[400:403]))