from datetime import date
print("\033[1;32mDesafio 54\033[m")
count = 0
ano = date.today().year

for c in range(1,8):
    nascimento = int(input(f"Digite a {c}° data: "))
    count += 1
    if (ano - nascimento) < 18:
        print(f"{c}° data, faltam alguns anos para você completar a maioridade.")
    else:
        print(f"{c}° data, você ja completou a maioridade")
