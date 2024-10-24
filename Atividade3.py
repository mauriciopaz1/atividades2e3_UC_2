import pandas as pd
import os
os.system('cls')


arquivo = 'vendas_roupas.xlsx'
dados_vendas = pd.read_excel(arquivo)

print("Primeiras 10 linhas dos dados de vendas:")
print(dados_vendas.head(10))

totaldeunidadesvendidas= dados_vendas['Unidades Vendidas'].sum()
print("\nSomatório total das quantidades vendidas:", totaldeunidadesvendidas)

mediapreçoporunidade = dados_vendas['Preço por Unidade (R$)'].mean()
print("Valor médio dos preços por unidade:", mediapreçoporunidade)

maiorfaturamento = dados_vendas['Faturamento Total (R$)'].max()

print('Maior faturamento total entre os produtos: ', maiorfaturamento)

menorfaturamento = dados_vendas['Faturamento Total (R$)'].min()

print('Menor faturamento total entre os produtos: ', menorfaturamento)

produtosbaixasatisfacao = dados_vendas[dados_vendas['Satisfação'] == 'Baixo']

print("\nPRODUTOS COM BAIXA SATISFAÇÃO:")
print(produtosbaixasatisfacao[["Produto", "Satisfação"]])


