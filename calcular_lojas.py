# Retornar a tabela com as lojas que mais vendem

import pandas as pd

def calcular_lojas_mais_vendem(tabela_total):
    tabela_lojas = tabela_total.groupby('Loja').sum()
    tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by='Faturamento', ascending=False)
    return tabela_lojas
