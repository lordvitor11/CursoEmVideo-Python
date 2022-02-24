print("\033[1;32mDesafio 50\033[m")
cont = 0
cont2 = 0
soma = 0

for c in range(1, 7):
    num = int(input(f"Digite o {c}° valor: "))
    cont += 1
    if num % 2 == 0:
        cont2 += 1
        soma += num
print(f"Você informou {cont} números e apenas {cont2} desses números são pares, então a soma de todos os números pares foi {soma}")
