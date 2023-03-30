# Dashboard de Vendas e Devoluções
- O projeto consiste em analisar dados de vendas e devoluções de várias cidades no Brasil, com objetivo de identificar qual produto gerou maior faturamento, qual produto teve mais devoluções e qual foi o valor de faturamento de cada item. Posteriormente o projeto será aperfeiçoado, adicionando novos gráficos e sugestões de decisão de negócio baseado nos resultados. Este repositório também conta com chaves de acesso e assinatura, contendo selo de verificado em cada commit.
# Processos envolvidos no projeto
- Importação de base de dados
- Tratamento e compilação das bases de dados
- Cálculo do produto mais vendido (em quantidade)
- Cálculo do produto que mais faturou (em faturamento)
- Cálculo da loja/cidade que mais vendeu (em faturamento)
# Bibliotecas utilizadas
- os
- pandas
- plotly.express
- plotly.subplots
- plotly.graph_objects
# Dashboard de Vendas
- Este projeto também inclui a criação de um dashboard interativo usando a biblioteca Plotly. O dashboard exibe gráficos de barras que mostram os produtos mais vendidos, os produtos que mais faturam e as lojas/cidades que mais vendem. O usuário pode interagir com os gráficos para ver informações mais detalhadas.
# Anotações e atualizações do progresso:
- Primeiro fiz a importação, tratamento e compilação da base de dados. Fiz também alguns cálculos de faturamento.
- Fiz alguns subplots e adicionei os gráficos aos subplots.
- Como o tempo está apertado e preciso voltar a estudar, pretendo continuar posteriormente e adicionar mais informações e gráficos.
- 28/03: Comecei aplicar alguns conceitos de módulos, porém não está finalizado. Consegui criar o modulo que importa os dados e chamar ele em um outro modulo onde são feitos os cálculos. Fiz alguns arquivos .txt para visualizar o resultado e criar as próximas classes, porém não estou conseguindo fazer o calculo da loja que mais vendeu em faturamento. Pelo que entendi preciso retornar o resultado do método anterior para usar nesse novo método... Procurei algo que possa usar de exemplo no conteúdo da faculdade mas não encontrei, estou tentando pensar em algo relacionando a lógica do conteúdo e a situação-problema. Estive pensando desde ontem, vou testar hoje. Irei tentar fazer pelo menos essa parte logo, ainda tenho conteúdos para estudar.
- 29/03: Consegui obter o retorno esperado nos módulos de importar os dados, ver quais produtos mais venderam, ver quais produtos mais faturaram e ver quais lojas mais faturaram. Fiz uma pasta com arquivos txt contendo os resultados de cada modulo. Porém, não estou conseguindo fazer o modulo 'criar_dashboard' funcionar (ou pelo menos testa-lo), preciso disso para chamar todos os módulos no principal (main) e obter o dashboard completo como na primeira versão do codigo. Tentei consultar o CHATGPT porém sem sucesso, vou voltar de onde parei nos estudos sobre Python e encontrar outra forma de obter esses resultados, mesmo que não seja por um Dashboard a primeiro momento, tento fazer um Dashboard convertendo outros dados para ele.
# Progresso visual:
## Visão geral
![Visão geral](imagens/Dashboard.png)
## Gráficos individuais
![Gráficos individuais](imagens/Dashboard-lojas-que-mais-vendem.png)
![Gráficos individuais](imagens/Dashboard-produtos-mais-vendidos.png)
![Gráficos individuais](imagens/Dashboard-produtos-que-mais-faturaram.png)
