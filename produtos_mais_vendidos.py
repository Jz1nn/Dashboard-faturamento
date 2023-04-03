# Calcula os produtos mais vendidos (quantidade vendida)

import pandas as pd
from importar_dados import ImportadorDados

class ProdutosMaisVendidos:
    def __init__(self, tabela_total):
        self.tabela_total = tabela_total

    def calcular_produtos_mais_vendidos(self):
        mais_vendidos = self.tabela_total.groupby('Produto')['Quantidade Vendida'].sum()
        mais_vendidos = mais_vendidos.sort_values(ascending=False)
        return mais_vendidos

# testar a classe
# importador = ImportadorDados()
# tabela_total = importador.importar_dados()
# produtos_mais_vendidos = ProdutosMaisVendidos(tabela_total)
# mais_vendidos = produtos_mais_vendidos.calcular_produtos_mais_vendidos()
# print(mais_vendidos.head(5))
