from ex111_module.utilidadesCeV.moeda import *

def leiaDinheiro(valor):
    valor.replace(",", ".")
    if str(valor).isnumeric() == True:
        resumo(int(valor), 80, 35)
        return False
    else:
        print("Valor inválido")
        return True
