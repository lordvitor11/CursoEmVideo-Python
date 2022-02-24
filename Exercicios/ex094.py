pessoas = []
media = 0

while True:
    pessoas_temp = {
        "nome":input("Nome: "),
        "sexo":input("Sexo: [M/F] ").upper(),
        "idade":int(input("Idade: "))
    }

    pessoas.append(pessoas_temp)

    if input("Quer continuar?(S/N) ").upper() == "S":
        del pessoas_temp
    else:
        print("="*20)
        break

for p in pessoas:
    media += p['idade']

print(f"{len(pessoas)} pessoa(s) cadastrada(s)")
print(f"A média de idade é de: {media / len(pessoas)}")
print("As mulheres foram:", end="")
for p in pessoas:
    if p['sexo'] == "F":
        print(f" {p['nome']}", end=" |")

print("")
print("")
print("Pessoas com idade acima da média: ")
for p in pessoas:
    if p['idade'] > media / len(pessoas):
        print(f"Nome: {p['nome']}; Sexo: {p['sexo']}; Idade: {p['idade']}")
