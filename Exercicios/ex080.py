numeros = []
for _ in range(5):
    numero = int(input("Digite um número: "))
    for chave, valor in enumerate(numeros):
        if numero < valor:
            numeros.insert(chave, numero)
            break
    else:
        numeros.append(numero)

print(f"Lista ordenada: {numeros}")