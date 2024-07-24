from modulos import menus_opcoes, func_gerais

def altera_tudo_item(cod, itens):
  menus_opcoes.alterar()
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
  print("|")
  itens[str(cod)] = [nome, categoria, marca, True]
  func_gerais.alterado()


def altera_nome(cod, itens):
  menus_opcoes.alterar()
  nome = input("| Nome do item      : ")
  nome = nome.upper()
  print("|")
  if nome.strip() == "":
    return False
  itens[cod][0] = nome
  func_gerais.alterado()


def altera_categoria(cod, itens):
  menus_opcoes.alterar()
  categoria = input("| Categoria do item : ")
  categoria = categoria.upper()
  if categoria.strip() == "":
    return False
  print("|")
  itens[cod][1] = categoria
  func_gerais.alterado()


def altera_marca(cod, itens):
  marca = input("| Marca do item     : ")
  marca = marca.upper()
  if marca.strip() == "":
    return False
  print("|")
  itens[cod][2] = marca
  func_gerais.alterado()
