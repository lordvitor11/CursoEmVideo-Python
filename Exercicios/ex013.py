#Capricho
print("Desafio 013")
#Váriaveis
salario = float(input("Você recebeu um aumento 15%, mas não sabe calcular o aumento. Eu posso calcular para você, é so me dizer quanto ganhava antes do aumento: "))
pAumento = 15
nSalario = salario + (salario * pAumento / 100)
aumento = nSalario - salario
#informações
print(f"Salário antes do reajuste: R${salario}! \nSalário atual: R${nSalario}! \nValor do aumento: R${aumento}!")
