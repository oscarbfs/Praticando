import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Dados.dados import Dados

alunosDf = pd.DataFrame(Dados.alunosDic)
atletas = pd.DataFrame(Dados.atletas)

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [1,2,3,4,5,6,7,8,9,10]

# plt.scatter(x, y)
# plt.show()

# x1 = np.arange(-1000,1000,1)

# plt.plot(x1, -x1**3 + 4)
# plt.show()

atletasMasculinos = atletas.loc[atletas['Sex'] == "M"]
plt.scatter(atletasMasculinos['Height'], atletasMasculinos['Weight'])
plt.show()

