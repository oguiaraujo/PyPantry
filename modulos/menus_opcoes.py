import os

def menu_pypantry():
  os.system("clear")
  print()
  print("+-----------------------+")
  print("|         MENU          |")
  print("|       PYPANTRY        |")
  print("+-----------------------+")
  print("| 1 - Itens             |")
  print("| 2 - Compras           |")
  print("| 3 - Retiradas         |")
  print("| 4 - Estoque           |")
  print("| 5 - Lista de Compras  |")
  print("| 6 - Relatórios        |")
  print("| 7 - Informações       |")
  print("| 0 - Sair              |")
  print("+-----------------------+")
  op_menu = input("| Escolha sua opção:")
  return op_menu


def menu_itens():
  os.system('clear')
  print()
  print("+----------------------+")
  print("|      MENU ITENS      |")
  print("+----------------------+")
  print("| 1 - Cadastrar        |")
  print("| 2 - Exibir           |")
  print("| 3 - Alterar          |")
  print("| 4 - Remover          |")
  print("| 0 - Voltar           |")
  print("+----------------------+")
  op_itens = input("| Escolha sua opção:")
  return op_itens


def menu_compras():
  os.system('clear')
  print()
  print("+----------------------+")
  print("|     MENU COMPRAS     |")
  print("+----------------------+")
  print("| 1 - Cadastrar        |")
  print("| 2 - Exibir           |") 
  print("| 3 - Alterar          |")
  print("| 4 - Remover          |")
  print("| 0 - Voltar           |")
  print("+----------------------+")
  op_compras = input("| Escolha sua opção:")
  return op_compras


def menu_retiradas():
  os.system('clear')
  print()
  print("+----------------------+")
  print("|    MENU RETIRADAS    |")
  print("+----------------------+")
  print("| 1 - Cadastrar        |")
  print("| 2 - Exibir           |")
  print("| 3 - Alterar          |")
  print("| 4 - Remover          |")
  print("| 0 - Voltar           |")
  print("+----------------------+")
  op_retiradas = input("| Escolha sua opção:")
  return op_retiradas


def cadastrar():
  os.system("clear")
  print()
  print("+-----------------------+")
  print("|       CADASTRAR       |")
  print("+-----------------------+")
  print("|")
  print("| <ENTER> para voltar")
  print("|")


def exibir():
  os.system("clear")
  print()
  print("+----------------------+")
  print("|        EXIBIR        |")
  print("+----------------------+")
  print("|")
  print("| <ENTER> para voltar")
  print("|")


def alterar():
  os.system("clear")
  print()
  print("+-----------------------+")
  print("|        ALTERAR        |")
  print("+-----------------------+")
  print("|")
  print("| <ENTER> para voltar")
  print("|")

# Opções de alterar inspiradas no PyBooks de Diego Axel
def aletrar_oque_item():
  os.system("clear")
  print()
  print("+--------------------+")
  print("|    O'QUE DESEJA    |")
  print("|      ALTERAR?      |")
  print("+--------------------+")
  print("| 1 - Tudo           |")
  print("| 2 - Nome           |")
  print("| 3 - Categoria      |")
  print("| 4 - Marca          |")
  print("| 0 - Nada           |")
  print("+--------------------+")
  op_alterar_oque = input("| Escolha sua opção:")
  return op_alterar_oque


def aletrar_oque_comp():
  os.system("clear")
  print()
  print("+--------------------+")
  print("|    O'QUE DESEJA    |")
  print("|      ALTERAR?      |")
  print("+--------------------+")
  print("| 1 - Tudo           |")
  print("| 2 - Valor          |")
  print("| 3 - Quantidade     |")
  print("| 0 - Nada           |")
  print("+--------------------+")
  op_alterar_oque = input("| Escolha sua opção:")
  return op_alterar_oque



def remover():
  os.system("clear")
  print()
  print("+-----------------------+")
  print("|        REMOVER        |")
  print("+-----------------------+")
  print("|")
  print("| <ENTER> para voltar")
  print("|")


def estoque():
  os.system('clear')
  print()
  print("+-------------------------------+")
  print("|            ESTOQUE            |")
  print("+-------------------------------+")
  print()


def lista_de_compras():
  os.system('clear')
  print()
  print("+------------------------------+")
  print("|       LISTA DE COMPRAS       |")
  print("+------------------------------+")
  print("")

def relatorios():
  os.system('clear')
  print()
  print("+-------------------------------+")
  print("|      RELATÓRIOS DE ITENS      |")
  print("+-------------------------------+")
  print("| 1 - Todos os itens            |")
  print("| 2 - Itens por categoria       |")
  print("| 3 - Itens por marca           |")
  print("| 4 - Todas as compras          |")
  print("| 5 - Compras por data          |")
  print("| 6 - Todas as retiradas        |")
  print("| 7 - Retiradas por data        |")
  print("| 0 - Voltar                    |")
  print("+-------------------------------+")
  op_relatorios = input("| Escolha sua opção:")
  return op_relatorios


def todos_itens():
  os.system('clear')
  print("+------------------------------+")
  print("|        TODOS OS ITENS        |")
  print("+------------------------------+")
  print()


def itens_por_categoria():
  os.system('clear')
  print("+-------------------------------+")
  print("|      ITENS POR CATEGORIA      |")
  print("+-------------------------------+")
  print("|")
  print("| <ENTER> para voltar")
  print()


def itens_por_marca():
  os.system('clear')
  print("+-------------------------------+")
  print("|        ITENS POR MARCA        |")
  print("+-------------------------------+")
  print("|")
  print("| <ENTER> para voltar")
  print()


def todas_compras():
  os.system('clear')
  print("+------------------------------+")
  print("|       TODOS AS COMPRAS       |")
  print("+------------------------------+")
  print()


def compras_por_data():
  os.system('clear')
  print("+------------------------------+")
  print("|       COMPRAS POR DATA       |")
  print("+------------------------------+")
  print("|")
  print("| <ENTER> para voltar")
  print()


def todas_retiradas():
  os.system('clear')
  print("+------------------------------+")
  print("|      TODOS AS RETIRADAS      |")
  print("+------------------------------+")
  print()


def retiradas_por_data():
  os.system('clear')
  print("+------------------------------+")
  print("|      RETIRADAS POR DATA      |")
  print("+------------------------------+")
  print()
