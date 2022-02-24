from random import randint
from time import sleep

def sorteia():
    print("Sorteando 5 valores da lista: ", end="")
    for c in range(5):
        numeros.append(randint(0, 10))
        print(numeros[c], end=" ", flush = True)
        sleep(1)
    print("PRONTO!")

def somaPar():
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num

    print(f"Somando os valores pares de {numeros}, temos {soma}")

numeros = []
sorteia()
somaPar()
