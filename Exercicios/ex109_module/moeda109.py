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
