print("\033[1;32mDesafio 52\033[m")
num = int(input("Digite um número: "))
count = 0

for c in range(1, num + 1):
    if num % c == 0:
        print(f"\033[33m{c}\033[m", end="")
        count += 1
    else:
        print(f"\033[31m{c}\033[m", end="")
    
if count == 2:
    print(f"\nO número {num} é divisível por {count} números, então {num} é primo")
else:
    print(f"\nO número {num} é divisível por {count} números, então {num} não é primo")
