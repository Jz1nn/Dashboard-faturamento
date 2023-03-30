# Calcular a lojas que mais venderam (em faturamento)

import pandas as pd

from importar_dados import importarDados

from produtos_mais_faturaram import produtosMaisFaturaram

class lojasMaisVenderam:
    def __init__(self, tabela_total_e_faturamento):
        self.tabela_total_e_faturamento = tabela_total_e_faturamento.copy()

    def calcular_lojas_mais_venderam(self):
        lojas_mais_venderam = self.tabela_total_e_faturamento.groupby('Loja').sum()
        lojas_mais_venderam = lojas_mais_venderam[['Faturamento']].sort_values(by='Faturamento', ascending=False)
        return lojas_mais_venderam
    
importador = importarDados()
tabela_total = importador.importar_dados()

# Calcula os produtos que mais faturaram
produtos_mais_faturaram = produtosMaisFaturaram(tabela_total)
mais_faturaram = produtos_mais_faturaram.calcular_tabela_total_e_faturamento()

# Calcula as lojas que mais venderam
lojas_mais_venderam = lojasMaisVenderam(mais_faturaram)
mais_venderam = lojas_mais_venderam.calcular_lojas_mais_venderam()

# Cria o arquivo de texto
with open('lojas_mais_venderam.txt', 'w') as arquivo:
    arquivo.write(mais_venderam.to_string())
