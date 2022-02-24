print("\033[1;32mDesafio 49\033[m")
num = int(input("Digite o número que você quer saber a tabuada: "))
multi = 0

for tabuada in range(11):
    resultado = multi * num
    print(f"{num} x {multi} = {resultado}")
    multi = multi +1
