from modulos import menus_opcoes, func_gerais

def altera_tudo_comp(compras, dt_hr, estoque):
  menus_opcoes.alterar()
  cod = compras[dt_hr][0]
  while True: # Aprendi com chatGPT
    try:
      valor = float(input("| Valor (R$) do item comprado : "))
      break
    except ValueError: # Aprendi com chatGPT
      print("| Insira um valor válido!")
      print("|")
  while True: # Aprendi com chatGPT
    try:
      estoque[cod] -= compras[dt_hr][2]
      quantidade = int(input("| Quantidade comprada         : "))
      print("|")
      break
    except ValueError: # Aprendi com chatGPT
      print("| Insira uma quantidade válida!")
      print("|")
  compras[str(dt_hr)] = [cod, valor, quantidade, True]
  estoque[cod] += quantidade
  func_gerais.alterado()


def altera_valor(compras, dt_hr):
  menus_opcoes.alterar()
  while True: # Aprendi com chatGPT
    try:
      valor = float(input("| Valor (R$) do item comprado : "))
      print("|")
      break
    except ValueError: # Aprendi com chatGPT
      print("| Insira um valor válido!")
      print("|")
  compras[dt_hr][1] = valor
  func_gerais.alterado()


def altera_quantidade(compras, dt_hr, estoque):
  menus_opcoes.alterar()
  cod = compras[dt_hr][0]
  while True: # Aprendi com chatGPT
    try:
      estoque[cod] -= compras[dt_hr][2]
      quantidade = int(input("| Quantidade comprada         : "))
      print("|")
      break
    except ValueError: # Aprendi com chatGPT
      print("| Insira uma quantidade válida!")
      print("|")
  compras[dt_hr][2] = quantidade
  estoque[cod] += quantidade
  func_gerais.alterado()