def manual(comando = ""):
    if comando == "":
        print("-------------------")
        print("Comando inválido")
        print("-------------------")
        return True
    elif comando == "fim":
        print("-----------")
        print("Até logo")
        print("-----------")
        return False
    else:
        print("----------------------------------------------------")
        print(f"Acessando o manual do comando '{comando}'")
        print("---------------------------------------------------")
        help(comando)
        return True

while manual(input("Função ou Bibliteca: ")):
    pass
