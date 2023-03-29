# Retornar as tabelas com os produtos mais vendidos e que mais faturaram

import pandas as pd

def calcular_produtos_vendidos(tabela_total):
    tabela_produtos = tabela_total.groupby('Produto').sum()
    tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
    return tabela_produtos

def calcular_faturamento_produtos(tabela_total):
    tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
    tabela_faturamento = tabela_total.groupby('Produto').sum()
    tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
    return tabela_faturamento
