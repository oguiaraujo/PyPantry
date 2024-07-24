import os
from modulos import func_alteraitem, menus_opcoes, func_gerais


def cadastra_item(itens):
  menus_opcoes.cadastrar()
  nome = input("| Nome do item      : ")
  nome = nome.upper()
  if nome.strip() == "":
    return False
  categoria = input("| Categoria do item : ")
  categoria = categoria.upper()
  if categoria.strip() == "":
    return False
  marca = input("| Marca do item     : ")
  marca = marca.upper()
  if marca.strip() == "":
    return False
  cod = func_gerais.gera_cod(itens)
  itens[str(cod)] = [nome, categoria, marca, True]
  func_gerais.cadastrado()
  

def exibe_item(itens):
  menus_opcoes.exibir()
  cod = input("| Insira o CÓDIGO do ITEM: ")
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
      print("| Codigo    :", cod)
      print("| Nome      :", itens[cod][0])
      print("| Categoria :", itens[cod][1])
      print("| Marca     :", itens[cod][2])
      print()
      input("<ENTER> para continuar")
  else:
    func_gerais.erro_cod()


def altera_item(itens):
  menus_opcoes.alterar()
  cod = input("| Insira o CÓDIGO do ITEM: ")
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
      op_alterar_oque = ""
      while op_alterar_oque != "0":
        op_alterar_oque = menus_opcoes.aletrar_oque_item()
        if op_alterar_oque == "1":
          func_alteraitem.altera_tudo_item(cod, itens)
        if op_alterar_oque == "2":
          func_alteraitem.altera_nome(cod, itens)
        if op_alterar_oque == "3":
          func_alteraitem.altera_categoria(cod, itens)
        if op_alterar_oque == "4":
          func_alteraitem.altera_marca(cod, itens)
  else:
    func_gerais.erro_cod()


def remove_item(itens, estoque):
  menus_opcoes.remover()
  cod = input("| Insira o CÓDIGO do ITEM: ")
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
      print("| Codigo    :", cod)
      print("| Nome      :", itens[cod][0])
      print("| Categoria :", itens[cod][1])
      print("| Marca     :", itens[cod][2])
    print()
    resp = input("| Deseja REMOVER o ITEM acima (S/N)?")
    if resp.upper() == "S":
      itens[cod][3] = False
      del estoque[cod]
      func_gerais.removido()
    else:
      return False
  else:
    func_gerais.erro_cod()