preços = ("Lápis", 1.75,
"Borracha", 2.00,
"Caderno", 15.90,
"Estojo", 5.00,
"Transferidor", 4.20,
"Compasso", 9.99,
"Mochila", 119.99,
"Canetas", 22.30,
"Livro", 34.90)
count = 0
count2 = 1

print("\033[1;32mListagem de preços\033[m")
for c in range(9):
    print(f"{preços[count]}............R$ {preços[count2]}")
    count += 2
    count2 += 2
