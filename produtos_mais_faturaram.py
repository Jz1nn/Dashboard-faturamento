# Calcula o produto que mais faturou (quantidade vendida * preço unitário)

import pandas as pd
from importar_dados import importarDados

class produtosMaisFaturaram:
    def __init__(self, tabela_total):
        self.tabela_total = tabela_total.copy()

    def calcular_produtos_mais_faturaram(self):
        tabela_faturamento = self.tabela_total.copy()
        tabela_faturamento['Faturamento'] = tabela_faturamento['Quantidade Vendida'] * tabela_faturamento['Preco Unitario']
        tabela_faturamento = tabela_faturamento.groupby('Produto')['Faturamento'].sum().reset_index()
        produtos_mais_faturaram = tabela_faturamento.sort_values(by='Faturamento', ascending=False)
        return produtos_mais_faturaram

    def calcular_tabela_total_e_faturamento(self):
        tabela_faturamento = self.tabela_total.copy()
        tabela_faturamento['Faturamento'] = tabela_faturamento['Quantidade Vendida'] * tabela_faturamento['Preco Unitario']
        tabela_faturamento = tabela_faturamento.groupby('Produto')['Faturamento'].sum().reset_index()
        mais_faturaram = tabela_faturamento.sort_values(by='Faturamento', ascending=False)
        tabela_total_e_faturamento = pd.merge(self.tabela_total, tabela_faturamento, on='Produto', how='left')
        return tabela_total_e_faturamento
