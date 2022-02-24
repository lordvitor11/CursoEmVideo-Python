num = []
for c in range(5):
    num.append(int(input(f"Digite o {c+1}° número: "))) 

print("Você digitou os números: ", end="")
for n in num:
    print(n, end=" ")

print(f"\nO menor valor digitado foi {min(num)} na {num.index(min(num))+1}° posição")
print(f"O maior valor digitado foi {max(num)} na {num.index(max(num))+1}° posição")
