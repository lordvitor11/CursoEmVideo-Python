from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print("Os valores sorteados foram:", end=" ")
for n in num: print(f"{n} ", end="")
print(f"\nO maior número é o: {max(num)}")
print(f"E o menor é o: {min(num)}")
