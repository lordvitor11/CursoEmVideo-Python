iniciar = 1

while iniciar == 1:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    r = int(input('''O que você quer fazer com esse valores?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
Sua escolha: '''))

    if r == 1:
        print(a+b)
        iniciar = 0
    elif r == 2:
        print(a*b)
        iniciar = 0
    elif r == 3:
        if a > b:
            print(f'O número {a} é o maior')
            iniciar = 0
        else:
            print(f'O número {b} é o maior')
            iniciar = 0
    elif r == 4:
        iniciar = 1
    elif r == 5:
        iniciar = 0
    else:
        print('Opção inválida, tente novamente!')
