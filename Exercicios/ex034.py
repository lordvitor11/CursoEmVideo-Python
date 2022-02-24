print("\033[0;32mDesafio 034\033[m")

salario = float(input("Quanto ganhava o funcionario? R$"))

if salario > 1250.00:
    print(f"Quem recebia R${salario} passará a receber R${salario + (salario * 10 / 100)}!")
if salario <= 1250.00:
    print(f"Quem recebia R${salario} passará a receber R${salario + (salario * 15 / 100)}!")
