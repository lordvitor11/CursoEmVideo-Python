lista = []
lista.append(int(input("Digite um valor: ")))

while True:
    choice = str(input("Você deseja continuar? (S/N) ")).upper()
    if choice == "S":
        num = int(input("Digite um valor: "))
        if num in lista:
            print("Número já existente, logo não será adicionado")
        else:
            lista.append(num)
            print("Valor adicionado com êxito")

    elif choice == "N":
        print(f"\nNúmeros armazenados: {sorted(lista)}")
        quit()
    else:
        print("Escolha inválida, tente novamente!", end=" ")
