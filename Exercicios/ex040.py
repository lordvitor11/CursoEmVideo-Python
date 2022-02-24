print("\033[1;32mDesafio 040\033[m")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Tirando {nota1:.1f} e {nota2:.1f} a média é {media:.1f}!")

if media < 5.00:
    print("\033[1;31mREPROVADO!\033[m")
elif media >= 5.00 and media <= 6.9:
    print("\033[1;33mRECUPERAÇÃO!\033[m")
else:
    print("\033[1;32mAPROVADO!\033[m")
