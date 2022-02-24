from ex107_module.moeda107 import *

valor = float(input("Digite o preço: R$"))
print(f"O dobro de {valor} é {dobro(valor)}")
print(f"A metade de {valor} é {metade(valor)}")
print(f"Aumentando 10%, temos {aumentar(valor, 10)}")
print(f"Reduzindo 13%, temos {diminuir(valor, 13)} ")
