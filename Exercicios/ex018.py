#Import's
import math
#Capricho
print("Desafio 016")
#Váriaveis
a = float(input("Digite o ângulo que você deseja: "))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
#Informações
print(f"Seno: {s:.2f}")
print(f"Cosseno: {c:.2f}")
print(f"Tangente: {t:.2f}")