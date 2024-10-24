import pandas as pd
import os 
os.system('cls')


produtos = ['Camiseta', 'Calça', 'Jaqueta', 'Vestido', 'Boné']
quantidades = [50, 30, 15, 10, 25]

estoque = pd.Series(quantidades, index=produtos)
print("Série de estoque inicial:")
print(estoque)

estoque['Saia'] = None
print("\nSérie de estoque com 'Saia':")
print(estoque)


mais_de_20 = estoque[estoque > 20]
print("\nProdutos com mais de 20 unidades em estoque:")
print(mais_de_20)


precos = [3500, 2500, 1200, 900, 1500]
estoque_precos = pd.Series(precos, index=produtos)

print("\nPreços dos produtos:")
print(estoque_precos)


valor_total_estoque = (estoque * estoque_precos).sum()

print("\nValor total do estoque: R$", valor_total_estoque)



