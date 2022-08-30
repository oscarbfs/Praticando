import matplotlib.pyplot as plt
import pandas as pd
from Dados.dados import Dados

alunosDf = pd.DataFrame(Dados.alunosDic)
atletas = pd.DataFrame(Dados.atletas)

atletasMasculinos = atletas.loc[atletas['Sex'] == "M"]
plt.scatter(atletasMasculinos['Height'], atletasMasculinos['Weight'])
plt.show()