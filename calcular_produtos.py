# Retornar as tabelas com os cálculos de produtos e lojas

import pandas as pd

from importar_dados import importarDados

class produtoMaisVendido:
    def __init__(self, tabela_total):
        self.tabela_total = tabela_total

    def calcular_produto_mais_vendido(self):
        tabela_produtos = self.tabela_total.groupby('Produto').sum()
        tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
        return tabela_produtos

class produtoMaisFaturou:
    def __init__(self, tabela_total):
        self.tabela_total = tabela_total

    def calcular_produto_mais_faturou(self):
        self.tabela_total['Faturamento'] = self.tabela_total['Quantidade Vendida'] * self.tabela_total['Preco Unitario']
        tabela_faturamento = self.tabela_total.groupby('Produto').sum()
        tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
        return self.tabela_total

    def adicionar_coluna_mais_faturou(self):
        self.tabela_total['Mais Faturou'] = self.tabela_total['Faturamento_x'] == self.tabela_total['Faturamento_y']
        self.tabela_total = self.tabela_total.merge(tabela_faturamento, on='Produto')
        return self.tabela_total
    

class lojaMaisVendeu:
    def __init__(self, tabela_total):
        self.tabela_total = tabela_total

    def calcular_loja_mais_vendeu(self):
        tabela_lojas = self.tabela_total.groupby('Loja').sum()
        tabela_lojas = tabela_lojas[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
        return tabela_lojas
    
importador = importarDados()
tabela_total = importador.importar_dados()

# Calcula os produtos mais vendidos
produtos_mais_vendidos = produtoMaisFaturou(tabela_total)
lista_produtos = produtos_mais_vendidos.calcular_produto_mais_faturou()[:4]

# Cria o arquivo de texto
with open('produtos_mais_.txt', 'w') as arquivo:
    arquivo.write(lista_produtos.to_string())