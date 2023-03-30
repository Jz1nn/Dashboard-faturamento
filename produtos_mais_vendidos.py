# Calcula os produtos mais vendidos

import pandas as pd
from importar_dados import importarDados

class produtosMaisVendidos:
    def __init__(self, tabela_total):
        self.tabela_total = tabela_total

    def calcular_produtos_mais_vendidos(self):
        mais_vendidos = self.tabela_total.groupby('Produto').sum()
        mais_vendidos = mais_vendidos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
        return mais_vendidos
