# Retornar tabela total com todos os dados

import os
import pandas as pd

class importarDados:
    def __init__(self):
        self.caminho = os.path.join(os.getcwd(), 'Vendas')

    def importar_dados(self):
        lista_arquivos = os.listdir(self.caminho)
        tabela_total = pd.DataFrame()
        
        for arquivo in lista_arquivos:
            if "Vendas" in arquivo:
                tabela = pd.read_csv(os.path.join(self.caminho, arquivo))
                tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)

        return tabela_total