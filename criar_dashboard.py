import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from importar_dados import importarDados
from produtos_mais_vendidos import produtosMaisVendidos
from produtos_mais_faturaram import produtosMaisFaturaram
from lojas_mais_venderam import lojasMaisVenderam

class CriarDashboard:
    def __init__(self, tabela_total, mais_vendidos, produtos_mais_faturaram, lojas_mais_venderam):
        self.tabela_total = tabela_total.copy()
        self.mais_vendidos = mais_vendidos.copy()
        self.produtos_mais_faturaram = produtos_mais_faturaram.copy()
        self.lojas_mais_venderam = lojas_mais_venderam.copy()

    def criar_dashboard(self):
        fig = make_subplots(rows=3, cols=2)
        fig.add_trace(go.Bar(x=self.mais_vendidos.index, y=self.mais_vendidos['Quantidade Vendida'], name='Produtos mais produtosMaisVendidos'), row=1, col=1)
        fig.add_trace(go.Bar(x= self.produtos_mais_faturaram.index, y= self.produtos_mais_faturaram['Faturamento'], name='Produtos que mais faturaram'), row=1, col=2)
        fig.add_trace(go.Bar(x= self.lojas_mais_venderam.index, y= self.lojas_mais_venderam['Faturamento'], name='Lojas que mais vendem'), row=2, col=1)
        fig.update_layout(height=800, width=800, title_text="Dashboard de Vendas")
        fig.show()
        return fig

# testar a classe
importador = importarDados()
tabela_total = importador.importar_dados()
produtos_mais_vendidos = produtosMaisVendidos(tabela_total)
mais_vendidos = produtos_mais_vendidos.calcular_produtos_mais_vendidos()
produtos_mais_faturaram = produtosMaisFaturaram(tabela_total)
produtos_mais_faturaram = produtos_mais_faturaram.calcular_produtos_mais_faturaram()
lojas_mais_venderam = lojasMaisVenderam(tabela_total)
lojas_mais_venderam = lojas_mais_venderam.calcular_lojas_mais_venderam()
criar_dashboard = CriarDashboard(tabela_total, mais_vendidos, produtos_mais_faturaram, lojas_mais_venderam)
criar_dashboard.criar_dashboard()

