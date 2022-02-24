def ficha(nome = input("Nome do jogador: "), gols = input("Número de gols: ")):
    if nome == "":
        nome = "<desconhecido>"

    if gols == "":
        gols = "0"

    return f"O jogador {nome} fez {gols} gol(s) no campeonato."

print(ficha())
