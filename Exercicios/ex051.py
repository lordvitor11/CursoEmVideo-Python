print("\033[1;32mDesafio 51\033[m")
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro +(10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(f"{c} ", end="-> ")
print("FIM!")
