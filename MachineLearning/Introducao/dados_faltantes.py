import matplotlib.pyplot as plt
import pandas as pd
from Dados.dados import Dados

alunosDf = pd.DataFrame(Dados.alunosDic)
atletas = pd.DataFrame(Dados.atletas)

atletasCompletos = atletas.dropna()
print(atletasCompletos.head())

nulos = atletas.isnull()
print(nulos.head())

faltantes = atletas.isnull().sum()
print(faltantes)

faltantesPercentual = (atletas.isnull().sum() / len(atletas['ID']))* 100
print(faltantesPercentual)

atletas['Medal'].fillna('Nenhuma', inplace=True)
atletas['Age'].fillna(int(atletas['Age'].mean()), inplace=True)
atletas['Height'].fillna(int(atletas['Height'].mean()), inplace=True)
atletas['Weight'].fillna(int(atletas['Weight'].mean()), inplace=True)
print(atletas.head())

faltantesPercentual = (atletas.isnull().sum() / len(atletas['ID']))* 100
print(faltantesPercentual)