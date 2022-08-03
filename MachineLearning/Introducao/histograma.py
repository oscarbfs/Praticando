import matplotlib.pyplot as plt
import pandas as pd
from Dados.dados import Dados

alunosDf = pd.DataFrame(Dados.alunosDic)
atletas = pd.DataFrame(Dados.atletas)

atletas.hist(column='Age', bins=100)
plt.show()

