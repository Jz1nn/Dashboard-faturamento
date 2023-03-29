# Retornar tabela total com os dados de todas as vendas

import os
import pandas as pd

def importar_dados():
    lista_arquivo = os.listdir(os.path.join(os.getcwd(), 'Vendas'))
    tabela_total = pd.DataFrame()
    for arquivo in lista_arquivo:
        if "Vendas" in lista_arquivo:
            tabela = pd.read_csv(os.path.join(os.getcwd(), 'Vendas', arquivo))
            tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)
    return tabela_total
