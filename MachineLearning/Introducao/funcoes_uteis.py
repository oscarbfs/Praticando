import pandas as pd
from Dados.dados import Dados

alunosDf = pd.DataFrame(Dados.alunosDic)

print(alunosDf)
print("\n")

print(alunosDf.head())
print("\n")

print(alunosDf.shape)
print("\n")

print(alunosDf.describe())
print("\n")
