print("\033[1;32mDesafio 48\033[m")

cont = 0
soma = 0
for c in range(1, 500, 2):
    print(c,end=" ")
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f"\nSoma de todos os {cont} valores solicitados é {soma}")            
