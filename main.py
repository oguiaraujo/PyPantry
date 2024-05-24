import os

op_menu = ""
while op_menu != "0":
  os.system("clear")
  print()
  print("+----------------------+")
  print("|         MENU         |")
  print("|       DESPENSA       |")
  print("+----------------------+")
  print("| 1 - Produtos         |")
  print("| 2 - Estoque          |") # codigo do produto e quantidade
  print("| 3 - Lista de Compras |")
  print("| 4 - Relatórios       |")
  print("| 5 - Informações      |")
  print("| 0 - Sair             |")
  print("+----------------------+")
  # AQUI terão Sinais de notificação existentes com base nos relatórios
  op_menu = input("| Escolha sua opção:")

  if op_menu == "1":
    os.system("Clear")
    op_prod = ""
    while op_prod != "0":
      os.system('clear')
      print()
      print("+----------------------+")
      print("|       PRODUTOS       |")
      print("+----------------------+")
      print("| 1 - Cadastrar        |") # Código do produto, nome, marca, categoria
      print("| 2 - Exibir Dados     |")
      print("| 3 - Compras          |") # data e hora (são a chave), cod, quantidade, valor
      print("| 4 - Retiradas        |") # data e hora (são a chave), cod, quantidade
      print("| 0 - Voltar           |")
      print("+----------------------+")
      op_prod = input("| Escolha sua opção:")

      if op_prod == "1":
        os.system("clear")
        print("+----------------------+")
        print("|  CADASTRAR PRODUTOS  |")
        print("+----------------------+")
        print("|")
        nome = input("| Nome:")
        print("|")
        cod = input("| Código:")
        print("|")
        categoria = input("| Categoria:")
        print("|")
        marca = input("| Marca:")
        print("Produto cadastrado com sucesso!")
        input("<ENTER> para voltar")
      
      elif op_prod == "2":
        os.system("clear")
        print("+----------------------+")
        print("|     EXIBIR DADOS     |")
        print("+----------------------+")
        print("|")
        print("| Nome:", nome)
        print("| Codigo:", cod)
        print("| Categoria:", categoria)
        print("| Marca:", marca)
        print()
        input("<ENTER> para voltar")
      
      elif op_prod == "3":
        os.system("clear")
        print("+----------------------+")
        print("|        COMPRA        |")
        print("+----------------------+")
        print("|")
        cod = input("| Código do produto:") # Se o produto comprado não possui código existente, deve ser cadastrado antes
        print("|")
        dt_hr = input("| Data e Hora da Compra:")
        print("|")
        valor = input("| Valor da unidade:")
        print("|")
        quantidade = input("| Quantidade comprada:")
        print("Compra cadastrada com sucesso!")
        input("<ENTER> para voltar")
      
      elif op_prod == "4":
        os.system("clear")
        print("+----------------------+")
        print("|       RETIRADA       |")
        print("+----------------------+")
        print("|")
        cod = input("| Código do produto:") # É necessário um código existente para que aconteça o cadastro de retirada do produto
        print("|")
        dt_hr = input("| Data e Hora da Retirada:")
        print("|")
        quantidade = input("| Quantidade Retirada:") 
        print("Retirada cadastrada com sucesso!")
        input("<ENTER> para voltar")


  if op_menu == "2":
    os.system('clear')
    op_est = ""
    print()
    print("+-------------------+")
    print("|      ESTOQUE      |")
    print("+-------------------+")
    # cod e quantidade
    op_est = input("| <ENTER> para voltar")

  if op_menu == "3":
    os.system('clear')
    op_list = ""
    print()
    print("+----------------------------+")
    print("|      LISTA DE COMPRAS      |")
    print("+----------------------------+")
    # Variável que recebe os itens que atingiram o estoque minimo
    op_list = input("| <ENTER> para voltar")


  if op_menu == "4":
    os.system("Clear")
    op_rel = ""
    while op_rel != "0":
      os.system('clear')
      print()
      print("+----------------------------+")
      print("|    RELATÓRIOS DE ITENS     |")
      print("+----------------------------+")
      print("| 1 - Alta Quantidade        |")
      print("| 2 - Baixa Quantidade       |")
      print("| 3 - Faltando               |")
      print("| 4 - Próximos do Vencimento |")
      print("| 5 - Vencidos               |")
      print("| 0 - Voltar                 |")
      print("+----------------------------+")
      op_rel = input("| Escolha sua opção:")

  if op_menu == "5":
    os.system('clear')
    op_inf = ""
    print()
    print("+-------------------------------------------+")
    print("|                INFORMAÇÕES                |")
    print("+-------------------------------------------+")
    print("| Projeto de Controle de Despensa Doméstica |")
    print("| Desenvolvedor: Guilherme Araújo / @0Haki  |")
    print("+-------------------------------------------+")
    op_inf = input("| <ENTER> para voltar")

print("Programa Encerrado!")