# Importar os modulos e executar as funções para gerar as tabelas

from importar_dados import importar_dados as impd
from calcular_produtos import CalculoProdutos
from calcular_lojas import CalculoLojas

tabela_total = impd().importar_dados()
tabela_produtos = CalculoProdutos(tabela_total).calcular_produtos_vendidos()
tabela_faturamento = CalculoProdutos(tabela_total).calcular_faturamento_produtos()
tabela_lojas = CalculoLojas(tabela_total).calcular_lojas_mais_vendem()
# Criar o grafico

from criar_grafico import criar_grafico

criar_grafico().criar_grafico(tabela_total)

