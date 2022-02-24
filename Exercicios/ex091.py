from random import randint
import time

result = {}
lista = []

print("Jogando os dados...")
time.sleep(2)

for c in range(4):
    a = (c + 1)
    jogador = "Jogador" + str(a)
    result[jogador] = randint(1, 6) 

for k, v in result.items():
    print(f"O {k} tirou {v} ")
    time.sleep(1)

for v in result.values():
    lista.append(v)

lista = sorted(lista, key = int, reverse = True)
print(" ")
print(f"Ranking dos jogadores sorteados:")

for c in range(4):
    a = (c + 1)
    jogador = "Jogador" + str(a)
    #print(f"{a}º lugar: {jogador} com {lista[c]}")
    print(f"{a}º lugar:", end=" ")
    if lista[c] == result[jogador]:
        print(f"{jogador} com {lista[c]}")
    else:
        b = 0
        while result[jogador] != lista[c]:
            b += 1
            jogador = "Jogador" + str(b)
        print(f"{jogador} com {lista[c]}")

    time.sleep(1)
