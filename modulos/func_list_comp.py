  

def exibe_lista_de_compras(estoque, itens):
  for cod, quantidade in estoque.items():
    if quantidade <= 5:
      print("| Codigo :", cod)
      print("| Nome   :", itens[cod][0])
      print("| Marca  :", itens[cod][2])
      print("")
  print()
  input("| <ENTER> para voltar")
