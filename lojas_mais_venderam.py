# Calcular a lojas (cidades) que mais venderam (em faturamento)

import pandas as pd
from importar_dados import ImportadorDados
from produtos_mais_vendidos import ProdutosMaisVendidos
from produtos_mais_faturaram import FaturamentoProdutos

class LojasMaisFaturaram:
    def __init__(self, tabela_total, tabela_faturamento):
        self.tabela_total = tabela_total
        self.tabela_faturamento = tabela_faturamento

    def faturamento_lojas(self):
        faturamento_lojas = self.tabela_total.groupby('Loja')['Faturamento'].sum().sort_values(ascending=False)
        return faturamento_lojas

# importador = ImportadorDados()
# tabela_total = importador.importar_dados()
# faturamento_produtos = FaturamentoProdutos(tabela_total)
# tabela_faturamento = faturamento_produtos.faturamento_produtos()
# faturamento_por_loja = LojasMaisFaturaram(tabela_total, tabela_faturamento)
# resultado = faturamento_por_loja.faturamento_lojas()
# print(resultado.head(5))
