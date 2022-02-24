#Import's
import random
#Capricho
print("Desafio 020")
#Váriaveis
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1,n2,n3,n4]
#Funções
random.shuffle(lista)
#Informação
print(f"A ordem será {lista}")
