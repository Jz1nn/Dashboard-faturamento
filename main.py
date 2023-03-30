from importar_dados import importarDados
from produtos_mais_vendidos import produtosMaisVendidos
from produtos_mais_faturaram import produtosMaisFaturaram
from lojas_mais_venderam import lojasMaisVenderam
from criar_dashboard import CriarDashboard

importador = importarDados()
tabela_total = importador.importar_dados()