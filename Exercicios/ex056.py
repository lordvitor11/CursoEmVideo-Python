data = []
media_idade = 0
mulheres = 0
maior_idade = ["", 0]

while len(data) < 4:
    temp_data = []
    print(f"{len(data) + 1}ª Pessoa")

    temp_data.append(input("Nome: "))
    temp_data.append(int(input("Idade: ")))
    temp_data.append(input("Sexo [M/F]: ").upper())

    data.append(temp_data)

for pessoa in data:
    media_idade += pessoa[1]
    if pessoa[2] == "M":
        if pessoa[1] > maior_idade[1]:
            maior_idade.clear()
            maior_idade.append(pessoa[0]), maior_idade.append(pessoa[1])
    else:
        if pessoa[1] < 20:
            mulheres += 1

print(f"A média de idade do grupo é de {media_idade / len(data)}")
print(f"O homem mais velho tem {maior_idade[1]} anos e se chama {maior_idade[0]}")
print(f"Ao todo são {mulheres} mulher(s) com menos de 20 anos")
