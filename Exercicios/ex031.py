print("Desafio 031")

distancia = float(input("Digite a distancia da viagem: "))
menor = distancia * 0.50
maior = distancia * 0.45

if distancia <= 200:
    print(f"O valor da viagem é de R${menor:.2f}!")
else:
    print(f"O valor da viagem é de R${maior:.2f}!")
