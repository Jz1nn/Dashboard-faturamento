# Criacao de um dashboard com os dados de vendas

import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from matplotlib import pyplot as plt
from importar_dados import ImportadorDados
from produtos_mais_vendidos import ProdutosMaisVendidos
from produtos_mais_faturaram import FaturamentoProdutos
from lojas_mais_venderam import LojasMaisFaturaram

class CriarDashboard:
    def __init__(self, tabela_total, mais_vendidos, tabela_faturamento, faturamento_lojas):
        self.tabela_total = tabela_total
        self.mais_vendidos = mais_vendidos
        self.tabela_faturamento = tabela_faturamento
        self.faturamento_lojas = faturamento_lojas
    
    def dashboardFaturamento(self):
        fig = make_subplots(rows=2, cols=2)
        fig.add_trace(go.Bar(x=self.mais_vendidos.index, y=self.mais_vendidos.values, name='Produtos mais vendidos (em quantidade)'), row=1, col=1)
        fig.add_trace(go.Bar(x=self.faturamento_lojas.index, y=self.faturamento_lojas.values, name='Lojas que mais vendem (em receita)'), row=1, col=2)
        fig.add_trace(go.Bar(x=self.tabela_faturamento.index, y=self.tabela_faturamento.values, name='Produtos que mais faturam (em receita)'), row=2, col=1)
        fig.update_layout(height=800, width=1000, title_text="Dashboard de Vendas")
        fig.show()
      
# testar a classe
# importador = ImportadorDados()
# tabela_total = importador.importar_dados()
# produtos_mais_vendidos = ProdutosMaisVendidos(tabela_total)
# mais_vendidos = produtos_mais_vendidos.calcular_produtos_mais_vendidos()
# faturamento_produtos = FaturamentoProdutos(tabela_total)
# tabela_faturamento = faturamento_produtos.faturamento_individual_produtos()
# faturamento_por_loja = LojasMaisFaturaram(tabela_total, tabela_faturamento)
# faturamento_lojas = faturamento_por_loja.faturamento_lojas()
# dashboard = CriarDashboard(tabela_total, mais_vendidos, tabela_faturamento, faturamento_lojas)
# dashboard.dashboardFaturamento()
