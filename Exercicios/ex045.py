import random, time
print("\033[1;32mDesafio 45\033[m")
print("\033[1;33m-=-\033[m" * 3)
print("\033[1;34mJOKENPÔ!\033[m")
print("\033[1;33m-=-\033[m" * 3)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual você escolhe? "))
itens = ("Pedra", "Papel", "Tesoura")
computador = random.randint(0,2)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PÔ")
time.sleep(1)
print(f"O computador jogou {itens[computador]}")
print(f"O jogador jogou {itens[jogador]}")

if computador == 0 and jogador == 0:
    print("EMPATE!")
elif computador == 0 and jogador == 1:
    print("O jogador venceu!")
elif computador == 0 and jogador == 2:
    print("O computador venceu!")
elif computador == 1 and jogador == 0:
    print("O computador venceu!")
elif computador == 1 and jogador == 1:
    print("EMPATE!")
elif computador == 1 and jogador == 2:
    print("O jogador venceu!")
elif computador == 2 and jogador == 0:
    print("O jogador venceu!")
elif computador == 2 and jogador == 1:
    print("O computador venceu!")
elif computador == 2 and jogador == 2:
    print("EMPATE!")
else:
    print("Essa opção não existe. Tente novamente!")
