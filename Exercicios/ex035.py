print("\033[0;32mDesafio 035\033[m")

r1 = float(input("Digite o primeiro comprimento: "))
r2 = float(input("Digite o segundo comprimento: "))
r3 = float(input("Digite o terceiro comprimento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR UM TRIÂNGULO!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!")
