import pandas as pd
from Dados.dados import Dados

alunosDf = pd.DataFrame(Dados.alunosDic)
atletas = pd.DataFrame(Dados.atletas)

print(alunosDf['Nome'])
print("\n")
print(atletas.head())
print("\n")

# Manipulando Colunas 
atletas.rename(columns={'Name': 'Nome', 'Sex': 'Sexo', 'Age': 'Idade'}, inplace=True)
print(atletas.head())
print("\n")
print(atletas['Medal'].value_counts())
print("\n")
print(atletas.describe())
print("\n")

# Deletando Colunas
atletas.drop(columns=['Sexo', 'Season', 'City'], inplace=True)
print(atletas.head())
print("\n")
