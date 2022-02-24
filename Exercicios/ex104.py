def leiaInt(num):
    if num.isnumeric() == True:
        print(f"Você acabou de digitar o número: {num}")
        return False
    else:
        print("ERRO! Digite um número inteiro válido.")
        return True

while leiaInt(input("Digite um número: ")):
    pass
