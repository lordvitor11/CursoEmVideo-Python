from ex109_module.moeda109 import *

valor = float(input("Digite um valor: R$"))
print(f"Aumentando 10%, temos {aumentar(valor, 10, True)}")
print(f"Reduzindo 13%, temos {diminuir(valor, 13, True)}")
print(f"O dobro de {moeda(valor)} é {dobro(valor, True)}")
print(f"A metade de {moeda(valor)} é {metade(valor, True)}")
