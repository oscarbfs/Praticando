import pandas as pd

class Dados: 
    atletas = pd.read_csv('C:/Users/oscar/Dev/Praticando/MachineLearning/Introducao/Dados/athlete_events.csv')

    exelTest = pd.read_excel('C:/Users/oscar/Dev/Praticando/MachineLearning/Introducao/Dados/excel_teste.xlsx')

    alunosDic = {
        'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
        'Nota': [4, 7, 5.5, 9],
        'Aprovado' : ['Não', 'Sim', 'Não', 'Sim'],
    }