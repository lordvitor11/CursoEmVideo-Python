#Capricho
print("Desafio 015")
#Váriaveis
dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos quilometros foram percorridos? "))
pago = (dias * 60) + (km * 0.15)
#Informações
print(f"O total a pagar é de R${pago:.2f}!")
