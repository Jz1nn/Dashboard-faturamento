# Retornar tabela total com todos os dados

import os
import pandas as pd

class ImportadorDados:
    def importar_dados(self):
        caminho = os.path.join(os.getcwd(), 'Vendas')
        lista_arquivos = [arquivo for arquivo in os.listdir(caminho) if "Vendas" in arquivo]
        tabela_total = pd.concat([pd.read_csv(os.path.join(caminho, arquivo)).drop(['Unnamed: 0', 'SKU', 'Primeiro Nome', 'Sobrenome', 'Unnamed: 8'], axis=1) for arquivo in lista_arquivos], ignore_index=True)
        return tabela_total

# testar a classe
# importador = ImportadorDados()
# tabela_total = importador.importar_dados()
# print(tabela_total.head(5))
