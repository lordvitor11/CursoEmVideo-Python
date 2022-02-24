print("\033[1;32mDesafio 43\033[m")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}!")

if imc < 18.5:
    print("Abaixo do peso!")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal!")
elif imc >= 25 and imc < 30:
    print("Sobrepeso!")
elif imc >= 30 and imc < 40:
    print("Obesidade!")
else:
    print("Obesidade mórbida!")
