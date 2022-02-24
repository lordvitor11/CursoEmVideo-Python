maior = 0
menor = 0

for p in range(5):
    peso = float(input(f"Digite o {p + 1}° peso: "))
    if peso > maior:
        maior = peso
    
    if menor == 0:
        menor = peso
    else:
        if peso < menor:
            menor = peso

print(f"O maior peso lido foi de {maior}")
print(f"O menor peso lido foi de {menor}")
