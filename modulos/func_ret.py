
from modulos import menus_opcoes, func_gerais


def cadastra_retirada(retiradas, itens, estoque):
  menus_opcoes.cadastrar()
  cod = input("| Insira o CÓDIGO do ITEM: ")
  print("|")
  if cod.strip() == "":
    return False
  elif cod in itens:
    if itens[cod][3] == False:
      print("| O ITEM correspondente foi REMOVIDO anteriormente!")
      print("| CADASTRE outra vez!")
      print()
      input("<ENTER> para continuar")
      return False
    else:
      while True: # Aprendi com chatGPT
        try:
          quantidade = int(input("| Quantidade retirada : "))
          print("|")
          break
        except ValueError: # Aprendi com chatGPT
          print("| Insira uma quantidade válida!")
          print("|")
      dt_hr = func_gerais.gera_data_hora()
      retiradas[str(dt_hr)] = [cod, quantidade, True]
      if estoque[cod] > quantidade:
        estoque[cod] -= quantidade
        if estoque[cod] == 0:
          del estoque[cod]
      else:
        print("| Quantidade insuficiente no estoque!")
        print("| Tente cadastrar uma compra antes.")
        return False
      func_gerais.cadastrado()
  else:
    func_gerais.erro_cod()


def exibe_retirada(retiradas, itens):
  menus_opcoes.exibir()
  print("| Insira o CÓDIGO no seguinte formato: (DDMMAAAAHHMMSS)")
  dt_hr = input("| Insira o CÓDIGO da RETIRADA: ")
  print("|")
  if dt_hr.strip() == "":
    return False
  elif dt_hr in retiradas:
    if retiradas[dt_hr][2] == False:
      print("| A RETIRADA correspondente foi REMOVIDA anteriormente!")
      print("| CADASTRE outra vez!")
      print()
      input("<ENTER> para continuar")
      return False
    else:
      cod = retiradas[dt_hr][0]
      print("| Codigo da retirada  :", dt_hr)
      print("| Código do item      :", retiradas[dt_hr][0])
      print("| Nome do item        :", itens[cod][0])
      print("| Quantidade retirada :", retiradas[dt_hr][1])
      print()
      input("<ENTER> para continuar")
  else:
    func_gerais.erro_cod()


def altera_retirada(retiradas, estoque):
  menus_opcoes.alterar()
  print("| Insira o CÓDIGO no seguinte formato: (DDMMAAAAHHMMSS)")
  dt_hr = input("| Insira o CÓDIGO da RETIRADA: ")
  print("|")
  if dt_hr.strip() == "":
    return False
  elif dt_hr in retiradas:
    if retiradas[dt_hr][2] == False:
      print("| A RETIRADA correspondente foi REMOVIDA anteriormente!")
      print("| CADASTRE outra vez!")
      print()
      input("<ENTER> para continuar")
      return False
    else:
      cod = retiradas[dt_hr][0]
      while True:
        try:
          estoque[cod] += retiradas[dt_hr][1]
          quantidade = int(input("| Quantidade retirada: "))
          print("|")
          break
        except ValueError:
          print("| Insira uma quantidade válida!")
          print("|")
      retiradas[dt_hr][1] = quantidade
      if estoque[cod] > quantidade:
        estoque[cod] -= quantidade
        if estoque[cod] == 0:
          del estoque[cod]
      else:
        print("| Quantidade insuficiente no estoque!")
        print()
      func_gerais.alterado()
  func_gerais.erro_cod()  


def remover_retirada(retiradas, itens, estoque):
  menus_opcoes.remover()
  print("| Insira o CÓDIGO no seguinte formato: (DDMMAAAAHHMMSS)")
  dt_hr = input("| Insira o CÓDIGO da RETIRADA: ")
  print("|")
  if dt_hr.strip() == "":
    return False
  elif dt_hr in retiradas:
    if retiradas[dt_hr][2] == False:
      print("| A RETIRADA correspondente foi REMOVIDA anteriormente!")
      print("| CADASTRE outra vez!")
      print()
      input("<ENTER> para continuar")
      return False
    else:
      cod = retiradas[dt_hr][0]
      print("| Codigo da compra    :", dt_hr)
      print("| Código do item      :", retiradas[dt_hr][0])
      print("| Nome do item        :", itens[cod][0])
      print("| Quantidade comprada :", retiradas[dt_hr][1])
      print()
      resp = input("| Deseja REMOVER a RETIRADA acima (S/N)?")
      if resp.upper() == "S":
        resp2 = input("| REMOVER TAMBÉM a QUANTIDADE RETIRADA do estoque (S/N)?")
        if resp2.upper() == "S":
          estoque[cod] -= retiradas[dt_hr][1]
          retiradas[dt_hr][2] = False
          func_gerais.removido()
        elif resp2.upper() == "N":
          retiradas[dt_hr][2] = False
          func_gerais.removido()
        else:
          return False
      else:
        return False
  else:
    func_gerais.erro_cod()