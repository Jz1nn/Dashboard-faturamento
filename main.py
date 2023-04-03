# Importar as classes dos outros módulos

from importar_dados import ImportadorDados
from produtos_mais_vendidos import ProdutosMaisVendidos
from produtos_mais_faturaram import FaturamentoProdutos
from lojas_mais_venderam import LojasMaisFaturaram
from criar_dashboard import CriarDashboard

def main():
    # Importar dados
    importador = ImportadorDados()
    tabela_total = importador.importar_dados()

    # Calcular produtos mais vendidos
    produtos_mais_vendidos = ProdutosMaisVendidos(tabela_total)
    mais_vendidos = produtos_mais_vendidos.calcular_produtos_mais_vendidos()

    # Calcular faturamento por produto
    faturamento_produtos = FaturamentoProdutos(tabela_total)
    tabela_faturamento = faturamento_produtos.faturamento_individual_produtos()

    # Calcular faturamento por loja
    faturamento_por_loja = LojasMaisFaturaram(tabela_total, tabela_faturamento)
    faturamento_lojas = faturamento_por_loja.faturamento_lojas()

    # Criar dashboard
    dashboard = CriarDashboard(tabela_total, mais_vendidos, tabela_faturamento, faturamento_lojas)
    dashboard.dashboardFaturamento()

if __name__ == '__main__':
    main()
