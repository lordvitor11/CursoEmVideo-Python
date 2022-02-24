def area(largura, comprimento):
    area = largura * comprimento
    print(f"A área de um terreno {largura}x{comprimento} é de {area}m².")

print("Controle de Terrenos")
print("---------------------------------")
area(float(input("LARGURA (m): ") ), float(input("COMPRIMENTO (m): ")))
