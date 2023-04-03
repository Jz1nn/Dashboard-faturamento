# Calcula o produtos que mais faturaram (faturamento)

import pandas as pd
from importar_dados import ImportadorDados

class FaturamentoProdutos:
    def __init__(self, tabela_total):
        self.tabela_total = tabela_total

    def faturamento_produtos(self):
        self.tabela_total['Faturamento'] = self.tabela_total['Quantidade Vendida'] * self.tabela_total['Preco Unitario']
        tabela_faturamento = self.tabela_total.groupby('Produto')['Faturamento'].sum().sort_values(ascending=False)
        return self.tabela_total

    def faturamento_individual_produtos(self):
        self.tabela_total['Faturamento'] = self.tabela_total['Quantidade Vendida'] * self.tabela_total['Preco Unitario']
        tabela_faturamento = self.tabela_total.groupby('Produto')['Faturamento'].sum().sort_values(ascending=False)
        return tabela_faturamento

# testar a classe
# importador = ImportadorDados()
# tabela_total = importador.importar_dados()
# resultado = FaturamentoProdutos(tabela_total)
# geral = resultado.faturamento_produtos()
# individual = resultado.faturamento_individual_produtos()
# print(individual.info())
# print(geral.head(5))
# print(individual.head(5))
