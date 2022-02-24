from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
print(f"Quem nasceu em {atual} tem {idade} anos em {atual}!")

if idade  == 18:
    print("Você tem que se alistar imediatemente!")
elif idade < 18:
    saldo = 18 - idade
    print(f"Você ainda não tem 18 anos, faltam {saldo} ano(s) para o alistamento.")
elif idade > 18:
    saldo = idade - 18
    print(f"Você já deveria ter se alistado há {saldo} ano(s).")
