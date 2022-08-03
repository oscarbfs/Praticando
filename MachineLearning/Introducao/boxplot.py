import matplotlib.pyplot as plt
import pandas as pd
from Dados.dados import Dados

alunosDf = pd.DataFrame(Dados.alunosDic)
atletas = pd.DataFrame(Dados.atletas)

atletas100 = atletas.head(100)
atletas100 = atletas100.dropna()
print(atletas100)


boxplot = plt.boxplot([atletas100['Age'], atletas100['Height'], atletas100['Weight']], vert = 1, patch_artist = False)

plt.show()