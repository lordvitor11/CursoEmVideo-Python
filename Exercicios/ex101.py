def voto(idade):
    import datetime
    anoAtual = datetime.datetime.now()
    anoAtual = anoAtual.date()
    anoAtual = anoAtual.strftime("%Y")

    idade = int(anoAtual) - idade

    if idade >= 18 and idade < 65:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."
    elif idade >= 16 and idade < 18 or idade >= 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: NÃO VOTA."

print(voto(int(input("Em que ano você nasceu? "))))
