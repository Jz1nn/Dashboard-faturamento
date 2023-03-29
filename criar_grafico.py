# Cria o Dashboard de Vendas

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def criar_dashboard(tabela_produtos, tabela_faturamento, tabela_lojas):
    fig = make_subplots(rows=2, cols=2)
    fig.add_trace(go.Bar(x=tabela_produtos.index, y=tabela_produtos['Quantidade Vendida'], name='Produtos mais vendidos'), row=1, col=1)
    fig.add_trace(go.Bar(x=tabela_faturamento.index, y=tabela_faturamento['Faturamento'], name='Produtos que mais faturam'), row=1, col=2)
    fig.add_trace(go.Bar(x=tabela_lojas.index, y=tabela_lojas['Faturamento'], name='Lojas que mais vendem'), row=2, col=1)
    fig.update_layout(height=800, width=1000, title_text="Dashboard de Vendas")
    return fig
