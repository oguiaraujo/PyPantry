import os

#-PyPantry----------------------------------------------------------------------

menu = ""
while menu != "0":
  os.system("clear")
  print("+----------------------+")
  print("|         MENU         |")
  print("|       DESPENSA       |")
  print("+----------------------+")
  print("| 1 - Gerenciar        |")
  print("| 2 - Relatórios       |")
  print("| 3 - Lista de Compras |")
  print("| 4 - Informações      |")
  print("| 0 - Sair             |")
  print("+----------------------+")
  # print("| Sinais de notificação existentes com base nos relatórios")
  menu = input("| Escolha sua opção:")

  if menu == "1":
    os.system("clear")
    opList = ""
    while opList != "0":
      os.system('clear')
      print("+----------------------+")
      print("|   GERENCIAR ITENS    |")
      print("+----------------------+")
      print("| 1 - Adicionar        |")
      print("| 2 - Remover          |")
      print("| 3 - Encontrar        |")
      print("| 4 - Visualizar       |")
      print("| 0 - Voltar           |")
      print("+----------------------+")
      opList = input("| Escolha sua opção:")

      if opList == "1":
        os.system("clear")
        # Laço para ficar adicionando itens até inserir "Sair"
        print("+----------------------+")
        print("|    ADICIONAR ITEM    |")
        print("+----------------------+")
        nome = input("| Nome do item:")
        categoria = input("| Categoria do item:")
        quantidade = input("| Quantidade a ser adicionada:")
        validade = input("| Validade do item:") # Apenas se o item tiver validade
        data_compra = input("| Data de compra do item:") #Essa variável deve ter
        #relação direta com a validade, pois pode haver o mesmo item comprado em
        #datas diferentes (consequentemente com validades diferentes)
        localizacao = input("| Localização do item:")
        print()
        print("Item adicionado com sucesso!")
        os.system("clear")
        # Def de visualizar a despensa atual
        input("<ENTER> para voltar")

  elif menu == "2":
    os.system("Clear")
    opList = ""
    while opList != "0":
      os.system('clear')
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
      opList = input("| Escolha sua opção:")

  elif menu == "3":
    os.system('clear')
    opList = ""
    print("+----------------------------+")
    print("|      LISTA DE COMPRAS      |")
    print("+----------------------------+")
    # Variável que recebe os itens que atingiram o estoque minimo
    opList = input("| <ENTER> para voltar")

  elif menu == "4":
    os.system('clear')
    opList = ""
    print("+-------------------------------------------+")
    print("|                INFORMAÇÕES                |")
    print("+-------------------------------------------+")
    print("| Projeto de Controle de Despensa Doméstica |")
    print("| Desenvolvedor: Guilherme Araújo / @0Haki  |")
    print("+-------------------------------------------+")
    opList = input("| <ENTER> para voltar")