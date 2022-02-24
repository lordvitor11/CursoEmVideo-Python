from ex108_module.moeda108 import *

valor = float(input("Digite um valor: R$"))
print(f"Aumentando 10%, temos {moeda(aumentar(valor, 10))}")
print(f"Reduzindo 13%, temos {moeda(diminuir(valor, 13))}")
print(f"O dobro de {moeda(valor)} é {moeda(dobro(valor))}")
print(f"A metade de {moeda(valor)} é {moeda(metade(valor))}")
