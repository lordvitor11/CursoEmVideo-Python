pessoas = []
temp = []

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))

    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]

        if temp[1] < menor:
            menor = temp[1]

    pessoas.append(temp[:])
    temp.clear()

    resposta = str(input("Deseja continuar? [S/N] ")).upper()
    if resposta == "S":
        pass
    elif resposta == "N":
        break
    else:
        print("Opção inválida, tente novamente!", end=" ")

print("-" * 30)
print(f"Ao todo foram cadastradas {len(pessoas)} pessoas")
print(f"O maior peso foi de {maior}Kg. Peso de: ", end="")