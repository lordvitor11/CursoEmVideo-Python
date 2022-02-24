from datetime import date

print("\033[1;32mDesafio 041\033[m")
ano = int(input("Em qual ano você nasceu? "))
resultado = date.today().year - ano
print(f"Quem nasceu em {ano} tem {resultado} anos")

if resultado <= 9:
    print("Classificação: Mirim!")
elif resultado > 9 and resultado <= 14:
    print("Classificação: Infantil!")
elif resultado > 14 and resultado <= 19:
    print("Classificação: Junior!")
elif resultado > 19 and resultado <= 20:
    print("Classificação: Sênior!")
elif resultado > 20:
    print("Classificação: Master!")
else:
    print("Categoria não identificada... Tente novamente!")
