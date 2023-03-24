import os
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Percorrer todos os arquivos da pasta base de dados (Vendas)

lista_arquivo = os.listdir('C:\\Users\\benbo\\OneDrive\\Área de Trabalho\\PROJETOS\\Dashboard-vendas-devolucoes\\Vendas')

# Importar base de dados de vendas para um DataFrame

tabela_total = pd.DataFrame()

# Tratamento e compilação das bases de dados

for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"C:\\Users\\benbo\\OneDrive\\Área de Trabalho\\PROJETOS\\PROJETOS\\Dashboard-vendas-devolucoes\\Vendas\\{arquivo}")
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

# Mostrar gráfico