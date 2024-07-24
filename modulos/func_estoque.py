

def exibe_estoque(estoque, itens):
    for cod, quantidade in estoque.items():
      if quantidade > 0:
        print("| Codigo     :", cod)
        print("| Nome       :", itens[cod][0])
        print("| Quantidade :", quantidade)
        print("")
    print()
    input("| <ENTER> para voltar")
