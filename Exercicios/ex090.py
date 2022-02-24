boletin = {}
boletin["nome"] = str(input("Digite o seu nome: "))
boletin["media"] = float(input("Insira a sua média: "))

if boletin["media"] >= 7:
    boletin["situação"] = "aprovado"
else:
    boletin["situação"] = "reprovado"

print(f"{boletin['nome']} teve a média de {boletin['media']} e foi {boletin['situação']}")
