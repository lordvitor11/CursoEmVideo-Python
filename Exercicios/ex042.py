print("\033[1;32mDesafio 042\033[m")

r1 = float(input("Digite o primeiro comprimento: "))
r2 = float(input("Digite o segundo comprimento: "))
r3 = float(input("Digite o terceiro comprimento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos PODEM FORMAR um triângulo ", end="")
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")
