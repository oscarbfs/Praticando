import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Dados.dados import Dados

x = np.arange(-1000,1000,1)
y1 = x**2
y2 = x**3
y3 = -x**2
y4 = -x**3
ys= [y1, y2, y3, y4]

figura = plt.figure(figsize=(5,5))

for num in range(4):
    figura.add_subplot(2, 2, num+1)
    plt.plot(x, ys[num])

plt.show()
