print("\033[0;32mDesafio 036\033[m")

casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Em quantos anos deseja financiar? "))
prestacao = casa / (anos * 12)
limite = salario * 30 / 100

if prestacao > limite:
    print(f"Para pegar uma casa de {casa} em {anos} anos a prestação será de R${prestacao:.2f}!")
    print("O salário não é suficiente, o finaciamento foi \033[1;31mRECUSADO!\033[m")
else:
    print(f"Para pegar uma casa de {casa} em {anos} anos a prestação será de R${prestacao:.2f}!")
    print("O financiamento foi \033[1;32mAPROVADO\033[m")
    