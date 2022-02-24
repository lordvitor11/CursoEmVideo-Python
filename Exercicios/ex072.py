numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", 
"Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    num = int(input("Digite um número de 0 a 20: "))
    if num >= 0 and num <= 20:
        print(f"Número por extenso: {numeros[num]}")

        while True:
            escolha = str(input("Você deseja continuar? (S/N) ")).upper()
            if escolha == "S":
                break
            elif escolha == "N":
                quit()
            else:
                print("Opção inválida, tente novamente!", end=" ")

    print("Tente novamente!", end=" ")
