print("Desafio 029")

vel = int(input("Digite a velocidade do carro: "))
multa = (vel - 80) * 7

if vel > 80:
    print(f"Você foi multado! E terá de pagar R${multa:.2f}!")
    print(f"OBS: R$7.00 a cada km acima do limite")
else:
    print("Você estava dentro dos limites!")
