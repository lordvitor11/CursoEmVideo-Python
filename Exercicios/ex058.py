from random import randint

r = 1

while r == 1:
    n = randint(0,10)
    r = int(input('Eu pensei em um número, tente adivinhar qual é: '))
    if r == n:
        print('Parabéns, você acertou!')
    else:
        print(f'Você errou! Eu pensei no numero {n} e você digitou {r}, tente novamente!')
        r = 1
