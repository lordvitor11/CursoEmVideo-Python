import random
print("Desafio 028")

n = random.randint(0,5)
nDigitado = int(input("O computador escolheu um número de 0 a 5, tente adivinhar: "))

if n == nDigitado:
    print("Parabéns, você ganhou")
else:
    print("Que pena! Não foi dessa vez, tente novamente!")
