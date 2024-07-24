from modulos import menus_opcoes

def exibe_todos_itens(itens):
  menus_opcoes.todos_itens()
  for cod, info in itens.items(): #Linha_adaptada_do_chatGPT
    if info[3] == True: #Linha_adaptada_do_chatGPT
      print("| Codigo    :", cod)
      print("| Nome      :", itens[cod][0])
      print("| Categoria :", itens[cod][1])
      print("| Marca     :", itens[cod][2])
      print()
  print()
  input("<ENTER> para continuar")


def exibe_itens_por_categoria(itens):
  menus_opcoes.itens_por_categoria()
  categoria_procurada = input("| Categoria: ")
  print("|")
  if categoria_procurada == "":
    return False
  for cod, info in itens.items(): #Linha_adaptada_do_chatGPT
    if info[3] == True: #Linha_adaptada_do_chatGPT
      if categoria_procurada.upper() in info[1].upper():
        print("| Codigo    :", cod)
        print("| Nome      :", itens[cod][0])
        print("| Categoria :", itens[cod][1])
        print("| Marca     :", itens[cod][2])
        print()
  print()
  input("| <ENTER> para voltar")


def exibe_itens_por_marca(itens):
  menus_opcoes.itens_por_marca()
  marca_procurada = input("| Marca: ")
  print()
  if marca_procurada == "":
    return False
  for cod, info in itens.items(): #Linha_adaptada_do_chatGPT
    if info[3] == True: #Linha_adaptada_do_chatGPT
      if marca_procurada.upper() in info[2].upper():
        print("| Codigo    :", cod)
        print("| Nome      :", itens[cod][0])
        print("| Categoria :", itens[cod][1])
        print("| Marca     :", itens[cod][2])
        print()
  print()
  input("| <ENTER> para voltar")


def exibe_todas_compras(compras, itens):
  menus_opcoes.todas_compras()
  for dt_hr, info in compras.items(): #Linha_adaptada_do_chatGPT
    if info[3] == True: #Linha_adaptada_do_chatGPT
      cod = compras[dt_hr][0]
      print("| Codigo da compra    :", dt_hr)
      print("| Código do item      :", compras[dt_hr][0])
      print("| Nome do item        :", itens[cod][0])
      print("| Valor do item       : R$", compras[dt_hr][1])
      print("| Quantidade comprada :", compras[dt_hr][2])
      print()
  print()
  input("<ENTER> para continuar")


def exibe_compras_por_data(compras, itens):
  menus_opcoes.compras_por_data()
  print("| Insira a data no seguinte formato: (DDMMAAAA)")
  data_procurada = input("| Data: ")
  print()
  if data_procurada == "":
    return False
  for dt_hr, info in compras.items(): #Linha_adaptada_do_chatGPT
    if info[3] == True: #Linha_adaptada_do_chatGPT
      if dt_hr.startswith(data_procurada): #Linha_adaptada_do_chatGPT
        cod = compras[dt_hr][0]
        print("| Codigo da compra    :", dt_hr)
        print("| Código do item      :", compras[dt_hr][0])
        print("| Nome do item        :", itens[cod][0])
        print("| Valor do item       : R$", compras[dt_hr][1])
        print("| Quantidade comprada :", compras[dt_hr][2])
        print()
  print()
  input("| <ENTER> para voltar")


def exibe_todas_retiradas(retiradas, itens):
  menus_opcoes.todas_retiradas()
  for dt_hr, info in retiradas.items(): #Linha_adaptada_do_chatGPT
    if info[2] == True: #Linha_adaptada_do_chatGPT
      cod = retiradas[dt_hr][0]
      print("| Codigo da retirada  :", dt_hr)
      print("| Código do item      :", retiradas[dt_hr][0])
      print("| Nome do item        :", itens[cod][0])
      print("| Quantidade retirada :", retiradas[dt_hr][1])
      print()
  print()
  input("<ENTER> para continuar")


def exibe_retiradas_por_data(retiradas, itens):
  menus_opcoes.retiradas_por_data()
  print("| Insira a data no seguinte formato: (DDMMAAAA)")
  data_procurada = input("| Data: ")
  print()
  if data_procurada == "":
    return False
  for dt_hr, info in retiradas.items(): #Linha_adaptada_do_chatGPT
    if info[2] == True: #Linha_adaptada_do_chatGPT
      if dt_hr.startswith(data_procurada): #Linha_adaptada_do_chatGPT
        cod = retiradas[dt_hr][0]
        print("| Codigo da retirada  :", dt_hr)
        print("| Código do item      :", retiradas[dt_hr][0])
        print("| Nome do item        :", itens[cod][0])
        print("| Quantidade retirada :", retiradas[dt_hr][1])
        print()
  print()
  input("| <ENTER> para voltar")
