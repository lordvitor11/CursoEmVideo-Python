def notas(* notas, sit = False):
    media = sum(notas) / len(notas)
    media = float(str(round(media, 2)))

    result = {"quantidade":len(notas),
              "maiorNota":max(notas),
              "menorNota":min(notas),
              "media":media}

    if sit:
        if media >= 7:
            result["situação"] = "BOA"
        elif media >= 5 and media < 7:
            result["situação"] = "RAZOÁVEL"
        else:
            result["situação"] = "RUIM"

    return result

print(notas(3.5, 2, 6.5, 2, 7, 4, sit = True))
