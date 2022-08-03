import pandas as pd
from Dados.dados import Dados

alunosDf = pd.DataFrame(Dados.alunosDic)

print(alunosDf.loc[[0]])
print("\n")
print(alunosDf.loc[[0,2]])
print("\n")
print(alunosDf.loc[0:2])
print("\n")
print(alunosDf.loc[alunosDf['Nome'] == 'Pedro'])
print("\n")

# Manipulando Linhas DataFrame
primeirasLinhas = alunosDf.loc[0:2]
print(primeirasLinhas)
print("\n")
alunosAprovados = alunosDf.loc[alunosDf['Aprovado'] == "Sim"]
print(alunosAprovados)
print("\n")