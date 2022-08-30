import matplotlib.pyplot as plt
import pandas as pd
from Dados.dados import Dados
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

gspc = pd.DataFrame(Dados.gspc)

print("\nPrintando o head inicial\n")
print(gspc.head())

print("\nRemovendo coluna Date e printando ultimas duas linhas\n")
gspc = gspc.drop('Date', axis = 1)
print(gspc[-2::])

# Simulando produção, colocando ultima linha como o que vai acontecer amanhã
print("\nDefinindo ultima linha como o que vai acontecer amanhã\n")
amanha = gspc[-1::]
print(amanha)

print("\nTirando a ultima linha da base de dados\n")
newgspc = gspc.drop(gspc[-1::].index, axis = 0)
print(newgspc.tail())

print("\nCriando Target\n")
newgspc['target'] = gspc['Close'][1:len(gspc)].reset_index(drop=True)
print(newgspc.tail())

print("\nArmazenando ultima linha do newgspc\n")
prev = newgspc[-1::].drop('target', axis=1)
print(prev)

print("\nCriando base de treino\n")
treino = newgspc.drop(newgspc[-1::].index, axis=0)
print(treino.tail())

print("\nTrocando o valor de target para 0 e 1\n")
treino.loc[treino['target'] > treino['Close'], 'target'] = 1
print(treino.tail())
treino.loc[treino['target'] != 1, 'target'] = 0
print(treino.tail())

# Separando as variaveis entre preditoras e variavel alvo
y = treino['target'] # variavel alvo
x = treino.drop('target', axis = 1) # variaveis preditoras

# Criando os cojuntos de dados de treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Criando modelo
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

# Imprimindo resultados
print("\nImprimindo resultados\n")
resultado = modelo.score(x_teste, y_teste)
print("Acuária: ", resultado)

# Prevendo dados
print("\nPrevendo dados\n")
print(modelo.predict(prev))

print("\nColocando target na linha prev\n")
prev['target'] = modelo.predict(prev)
print(prev)

print("\nColocando previsão na base de dados\n")
newgspc = newgspc.append(amanha, sort=True)
print(newgspc.tail())
