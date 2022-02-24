print("\033[1;32mDesafio 038\033[m")

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    print(f"O primeiro valor é o maior, pois {valor1} é maior que {valor2}!")
elif valor1 == valor2:
    print("Não existe valor maior. Os dois são iguais!")
else:
    print(f"O maior valor é o segundo, pois {valor2} é maior que {valor1}!")
