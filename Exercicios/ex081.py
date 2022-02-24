num = []
a = int(input("Digite um número: "))
num.append(a)
while True:
    choice = str(input("Deseja continuar? (S/N) ")).upper()
    if choice == "S":
        a = int(input("Digite um outro número: "))
        num.append(a)
    elif choice == "N":
        print(f"Lista ordenada em ordem decrescente: {sorted(num, reverse=True)}")
        print(f"Você digitou {len(num)} elementos")
        if 5 in num:
            print(f"O número 5 está na lista")
        else:
            print("O número 5 não está na lista")
        
        quit()
        
    else:
        print("Opção inválida, tente novamente!", end=" ")
