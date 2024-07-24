import os
from modulos import func_alteracomp, menus_opcoes, func_gerais


def cadastra_compra(compras, itens, estoque):
  menus_opcoes.cadastrar()
  cod = input("| Insira o código do item: ")
  print("|")
  if cod.strip() == "":
    return False
  elif cod in itens:
    if itens[cod][3] == False:
      print("| O item correspondente foi removido anteriormente!")
      print("| Cadastre outra vez!")
      print()
      input("<ENTER> para continuar")
      return False
    else:
        while True: # Aprendi com chatGPT
          try:
            valor = float(input("| Valor (R$) do item comprado : "))
            break
          except ValueError: # Aprendi com chatGPT
            print("| Insira um valor válido!")
            print("|")
        while True: # Aprendi com chatGPT
          try:
            quantidade = int(input("| Quantidade comprada         : "))
            print("|")
            break
          except ValueError: # Aprendi com chatGPT
            print("| Insira uma quantidade válida!")
            print("|")
        dt_hr = func_gerais.gera_data_hora()
        compras[str(dt_hr)] = [cod, valor, quantidade, True]
        if cod in estoque:
          estoque[cod] += quantidade
        else:
          estoque[cod] = quantidade
        func_gerais.cadastrado()
  else:
    func_gerais.erro_cod()


def exibe_compra(compras, itens):
  menus_opcoes.exibir()
  print("| Insira o CÓDIGO no seguinte formato: (DDMMAAAAHHMMSS)")
  dt_hr = input("| Insira o CÓDIGO da COMPRA: ")
  print("|")
  if dt_hr.strip() == "":
    return False
  elif dt_hr in compras:
    if compras[dt_hr][3] == False:
      print("| A COMPRA correspondente foi REMOVIDA anteriormente!")
      print("| CADASTRE outra vez!")
      print()
      input("<ENTER> para continuar")
      return False
    else:
      cod = compras[dt_hr][0]
      print("| Codigo da compra    :", dt_hr)
      print("| Código do item      :", compras[dt_hr][0])
      print("| Nome do item        :", itens[cod][0])
      print("| Valor do item       : R$", compras[dt_hr][1])
      print("| Quantidade comprada :", compras[dt_hr][2])
      print()
      input("<ENTER> para continuar")
  else:
    func_gerais.erro_cod()


def altera_compra(compras, estoque):
  menus_opcoes.alterar()
  print("| Insira o CÓDIGO no seguinte formato: (DDMMAAAAHHMMSS)")
  dt_hr = input("| Insira o CÓDIGO da COMPRA: ")
  print("|")
  if dt_hr.strip() == "":
    return False
  elif dt_hr in compras:
    if compras[dt_hr][3] == False:
      print("| A COMPRA correspondente foi REMOVIDA anteriormente!")
      print("| CADASTRE outra vez!")
      print()
      input("<ENTER> para continuar")
      return False
    else:
      op_alterar_oque = ""
      while op_alterar_oque != "0":
        op_alterar_oque = menus_opcoes.aletrar_oque_comp()
        if op_alterar_oque == "1":
          func_alteracomp.altera_tudo_comp(compras, dt_hr, estoque)
        if op_alterar_oque == "2":
          func_alteracomp.altera_valor(compras, dt_hr)
        if op_alterar_oque == "3":
          func_alteracomp.altera_quantidade(compras, dt_hr, estoque)
  else:
    func_gerais.erro_cod()  


def remove_compra(compras, itens, estoque):
  menus_opcoes.remover()
  print("| Insira o CÓDIGO no seguinte formato: (DDMMAAAAHHMMSS)")
  dt_hr = input("| Insira o CÓDIGO da COMPRA: ")
  print("|")
  if dt_hr.strip() == "":
    return False
  elif dt_hr in compras:
    if compras[dt_hr][3] == False:
      print("| A COMPRA correspondente foi REMOVIDA anteriormente!")
      print("| CADASTRE outra vez!")
      print()
      input("<ENTER> para continuar")
      return False
    else:
      cod = compras[dt_hr][0]
      print("| Codigo da compra    :", dt_hr)
      print("| Código do item      :", compras[dt_hr][0])
      print("| Nome do item        :", itens[cod][0])
      print("| Valor do item       : R$", compras[dt_hr][1])
      print("| Quantidade comprada :", compras[dt_hr][2])
      print()
      resp = input("| Deseja REMOVER a COMPRA acima (S/N)?")
      if resp.upper() == "S":
        resp2 = input("| REMOVER TAMBÉM a quantidade comprada do estoque (S/N)?")
        if resp2.upper() == "S":
          estoque[cod] -= compras[dt_hr][2]
          compras[dt_hr][3] = False
          func_gerais.removido()
        elif resp2.upper() == "N":
          compras[dt_hr][3] = False
          func_gerais.removido()
        else:
          return False
      else:
        return False
  else:
    func_gerais.erro_cod()