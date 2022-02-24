numeros = []
pares = []
impares = []
count = 0

while True:
    num = int(input("Digite um número: "))
    numeros.append(num)
    choice = str(input("Deseja continuar? [S/N] ")).upper()
    if choice == "S":
        pass
    elif choice == "N":
        break
    else:
        print("Opção inválida, tente novamente!", end=" ")

for n in numeros:
    if (numeros[count]) % 2 == 0:
        pares.append(numeros[count])
    else:
        impares.append(numeros[count])
    count += 1

print(f"Lista completa: {sorted(numeros)}")
print(f"Lista separada em pares: {sorted(pares)}")
print(f"Lista separada em ímpares: {sorted(impares)}")
