import os
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Percorrer todos os arquivos da pasta base de dados (Vendas)

lista_arquivo = os.listdir(os.path.join(os.getcwd(), 'Vendas'))

# Importar base de dados de vendas para um DataFrame

tabela_total = pd.DataFrame()

# Tratamento e compilação das bases de dados

for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(os.path.join(os.getcwd(), 'Vendas', arquivo))
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)

# Calcular o produto mais vendido (em quantidade)

tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)

# Calcular o produto que mais faturou (em faturamento)

tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)

# Calcular a loja/cidade que mais vendeu (em faturamento)

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[["Faturamento"]].sort_values(by="Faturamento", ascending=False)

# Criar subplots
fig = make_subplots(rows=2, cols=2)

# Adicionar gráficos aos subplots
fig.add_trace(go.Bar(x=tabela_produtos.index, y=tabela_produtos['Quantidade Vendida'], name='Produtos mais vendidos'), row=1, col=1)
fig.add_trace(go.Bar(x=tabela_faturamento.index, y=tabela_faturamento['Faturamento'], name='Produtos que mais faturam'), row=1, col=2)
fig.add_trace(go.Bar(x=tabela_lojas.index, y=tabela_lojas['Faturamento'], name='Lojas que mais vendem'), row=2, col=1)

# Atualizar layout dos subplots
fig.update_layout(height=800, width=1000, title_text="Dashboard de Vendas")

# Mostrar gráfico
fig.show()