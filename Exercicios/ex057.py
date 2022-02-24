while True:
    sexo = input("Informe seu sexo: [M/F] ").upper()
    
    if sexo == "M":
        break
    elif sexo == "F":
        break
    else:
        print("Dados inválidos. Por favor,", end = " ")

print(f"Sexo {sexo} registrado com sucesso!")
