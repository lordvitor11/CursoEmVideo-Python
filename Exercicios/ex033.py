print("\033[0;32mDesafio 033\033[m")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
menor = a
maior = c 
#Verificando o menor
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando o maior
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f"O menor número foi o {menor}!")
print(f"O maior número foi o {maior}!")
