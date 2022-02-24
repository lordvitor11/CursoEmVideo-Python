print("\033[1;32mDesafio 44\033[m")
produto = float(input("Digite o valor: R$"))
a_vista = produto - (produto * 10 / 100)
a_vistaC = produto - (produto * 5 / 100)
parcela = produto / 2
juros = produto + (produto * 20 / 100)
escolha = int(input('''
[ 1 ] À vista dinheiro/cheque com 10% de desconto
[ 2 ] À vista no cartão com 5% de desconto
[ 3 ] Até 2 vezes no cartão sem juros
[ 4 ] 3 vezes ou mais no cartão com 20% de juros
'''))

if escolha == 1:
    print(f"Seu produto custava {produto} e com o desconto passou a custar {a_vista}.")
elif escolha == 2:
    print(f"Seu produto custava {produto} e com o desconto passou a custar {a_vistaC}.")
elif escolha == 3:
    print(f"Você pagará o seu produto em duas parcelas de R${parcela}.")
elif escolha == 4:
    n_parcela = int(input("Em quantas parcelas você dejesa pagar? "))
    print(f"Você pagará R${juros} dividido em {n_parcela} parcelas de R${juros / n_parcela}!")
else:
    print("Opção invalida. Tente novamente!")
