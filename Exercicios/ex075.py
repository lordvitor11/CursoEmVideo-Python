count = 0
num = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: ")), int(input("Digite o último número: ")))
print(f"Você digitou os valores: {num}")
print(f"O valor 9 apareceu {num.count(9)} vez(es)")
if 3 in num: print(f"O valor 3 apareceu pela primeira vez na {num.index(3)+1}ª posição")
else: print("O número 3 não foi encontrado em nenhuma posição")
for n in num:   
    if n % 2 == 0: 
        count += 1
print(f"Desses 4 números digitados, {count} são pares")
