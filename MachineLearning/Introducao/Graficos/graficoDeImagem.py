from matplotlib import image
from skimage.io import imread
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


endereco = 'C:/Users/oscar/Dev/Praticando/MachineLearning/Introducao/Dados/'
imagens= ['imagem1.jpg', 'imagem2.png']
enderecoImagens = []

for num in range(2):
    imagem = imread(endereco+str(imagens[num]))
    enderecoImagens.append(imagem)

figura = plt.figure(figsize=(10,5))
for num in range(2):
    figura.add_subplot(1, 2, num+1)
    plt.imshow(enderecoImagens[num])

plt.show()