def aumentar(valor = 0, percentual = 0, format = False):
    res = valor + (valor * percentual / 100)
    return res if format == False else moeda(res)

def diminuir(valor = 0, percentual = 0, format = False):
    res = valor - (valor * percentual / 100)
    return res if format == False else moeda(res)

def dobro(valor = 0, format = False):
    res = valor * 2
    return res if format == False else moeda(res)

def metade(valor = 0, format = False):
    res = valor / 2
    return res if format == False else moeda(res)

def moeda(valor = 0, moeda = "R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")

def resumo(valor = 0, aumento = 0, reducao = 0):
    print("----------------------------------------------------")
    print("                  RESUMO DO VALOR")
    print("----------------------------------------------------")
    print(f"Preço analisado:          {moeda(valor)}")
    print(f"Dobro do preço:           {dobro(valor, True)}")
    print(f"Metade do preço:          {metade(valor, True)}")
    print(f"{aumento}% de aumento:           {aumentar(valor, aumento, True)}")
    print(f"{reducao}% de redução:           {diminuir(valor, reducao, True)}")
    print("----------------------------------------------------")
