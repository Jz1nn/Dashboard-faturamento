# Importar os modulos e executar as funções para gerar as tabelas

import importar_dados
import calcular_produtos
import calcular_lojas
import criar_grafico

tabela_total = importar_dados.importar_dados()
tabela_produtos = calcular_produtos.calcular_produtos_vendidos(tabela_total)
tabela_faturamento = calcular_produtos.calcular_faturamento_produtos(tabela_total)
tabela_lojas = calcular_lojas.calcular_lojas_mais_vendem(tabela_total)
fig = criar_grafico.criar_dashboard(tabela_produtos, tabela_faturamento, tabela_lojas)
fig.show()

# Salvar o dashboard em um arquivo html
fig.write_html('dashboard.html')
