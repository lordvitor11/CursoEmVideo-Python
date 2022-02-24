def leiaInt():
    global fluxo, num
    try:
        n = int(input("Digite um número inteiro: "))
    except (ValueError, TypeError):
        print("O valor informado não é válido, tente novamente!")
    except KeyboardInterrupt:
        print("\nO usuário preferiu não informar o valor")
        fluxo = False
        num = 0
    else:
        num = n
        fluxo = False

def leiaFloat(n1):
    global fluxo2
    try:
        n = float(input("Digite um número real: "))
    except (ValueError, TypeError):
        print("O valor informado não é válido, tente novamente!")
    except KeyboardInterrupt:
        print("\nO usuário preferiu não informar o valor")
        n = 0
        print(f"Número inteiro informado: {n1}")
        print(f"Número real informado: {n}")
        fluxo2 = False
    else:
        print(f"Número inteiro informado: {n1}")
        print(f"Número real informado: {n}")
        fluxo2 = False

fluxo = True
fluxo2 = True
num = 0
while fluxo2:
    if fluxo:
        leiaInt()
    else:
        leiaFloat(num)

print("Tenha um bom dia! :D")
