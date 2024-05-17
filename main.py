# Projeto Sistema de Controle de Despensa Doméstica
import os
import pickle
#-Dicionários-------------------------------------------------------------------
alimentos = {}
bebidas = {}
hpessoals = {}
plimpezas = {}
ferramentas = {}
#-Abrindo ou criando o arquivo da despensa com Pickle---------------------------
try:
  arq_alimentos = open("arq_alimentos.dat", "rb")
  alimentos = pickle.load(arq_alimentos)
except:
  arq_alimentos = open("arq_alimentos.dat", "wb")
arq_alimentos.close()

try:
  arq_bebidas = open("arq_bebidas.dat", "rb")
  bebidas = pickle.load(arq_bebidas)
except:
  arq_bebidas = open("arq_bebidas.dat", "wb")
arq_bebidas.close()

try:
  arq_hpessoals = open("arq_hpessoals.dat", "rb")
  hpessoals = pickle.load(arq_hpessoals)
except:
  arq_hpessoals = open("arq_hpessoals.dat", "wb")
arq_hpessoals.close()

try:
  arq_plimpezas = open("arq_plimpezas.dat", "rb")
  plimpezas = pickle.load(arq_plimpezas)
except:
  arq_plimpezas = open("arq_plimpezas.dat", "wb")
arq_plimpezas.close()

try:
  arq_ferramentas = open("arq_ferramentas.dat", "rb")
  ferramentas = pickle.load(arq_ferramentas)
except:
  arq_ferramentas = open("arq_ferramentas.dat", "wb")
arq_ferramentas.close()
#-Minhas Definições-------------------------------------------------------------
def exibir_alimentos():
  print("+--------------------+")
  print("|  Alimentos         |")
  print("+--------------------+")
  for alimento, quantidade in alimentos.items():
    print("| ",alimento,"|",quantidade)
  print("+--------------------+")


def exibir_bebidas():
  print("+--------------------+")
  print("|  Bebidas           |")
  print("+--------------------+")
  for bebida, quantidade in bebidas.items():
    print("| ",bebida,"|",quantidade)
  print("+--------------------+")

def exibir_hpessoals():
  print("+----------------------+")
  print("|  Higiene Pessoal     |")
  print("+----------------------+")
  for hpessoal, quantidade in hpessoals.items():
    print("| ",hpessoal,"|",quantidade)
  print("+----------------------+")

def exibir_plimpezas():
  print("+-----------------------+")
  print("|  Produtos de Limpeza  |")
  print("+-----------------------+")
  for plimpeza, quantidade in plimpezas.items():
    print("| ",plimpeza,"|",quantidade)
  print("+-----------------------+")

def exibir_ferramentas():
  print("+----------------------+")
  print("|  Ferramentas         |")
  print("+----------------------+")
  for ferramenta, quantidade in ferramentas.items():
    print("| ",ferramenta,"|",quantidade)
  print("+----------------------+")


menu = ''
while menu != "0":
  os.system('clear')
  print("+----------------------+")
  print("|         MENU         |")
  print("| Controle de Despensa |")
  print("+----------------------+")
  print("| 1 - Exibir todos     |")
  print("| 2 - Alimentos        |")
  print("| 3 - Bebidas          |")
  print("| 4 - H. Pessoal       |")
  print("| 5 - P. Limpeza       |")
  print("| 6 - Ferramentas      |")
  print("| 0 - Sair             |")
  print("+----------------------+")
  menu = input("| Escolha sua opção:")

  if menu == "1":
    os.system("clear")
    print()
    print("+--------------------+")
    print("|  Todos os Itens    |")
    print("+--------------------+")
    exibir_alimentos()
    exibir_bebidas()
    exibir_hpessoals()
    exibir_plimpezas()
    exibir_ferramentas()
    print()
    input("<ENTER> para voltar ao inicio")

  elif menu == "2":
    opLista = " "
    while opLista != "0":
      os.system("clear")
      print()
      print("+--------------------+")
      print("|     Alimentos      |")
      print("+--------------------+")
      print("| 1 - Adicionar      |")
      print("| 2 - Remover        |")
      print("| 3 - Exibir         |")
      print("| 0 - Voltar ao MENU |")
      print("+--------------------+")
      opLista = input("| Escolha uma opção:")

      if opLista == "1":
        os.system("clear")
        while True:
          print("Digite 'SAIR' para voltar")
          print()
          exibir_alimentos()
          alimento = input("Adicionar Alimento:")
          if alimento.upper() == "SAIR":
            break
          elif alimento.isdigit():
            print("Insira um nome válido")
            print()
          elif alimento.strip() == '':
            print("Insira um nome válido")
            print()
          else:
            alimento
            while True:
              try:
                quantidade = float(input("Quantidade a ser adicionada:"))
                print()
                break
              except ValueError:
                print("Insira uma quantidade válida")
                print()
            if alimento in alimentos:
              alimentos[alimento] += quantidade
            else:
              alimentos[alimento] = quantidade
        os.system("clear")
        exibir_alimentos()
        print()
        input("<ENTER> para voltar")

      elif opLista == "2":
        os.system("clear")
        while True:
          print("Digite 'SAIR' para voltar")
          print()
          exibir_alimentos()
          alimento = input("Remover Alimento:")
          if alimento.upper() == "SAIR":
            break
          elif alimento.isdigit():
            print("Insira um nome válido")
            print()
          elif alimento.strip() == '':
            print("Insira um nome válido")
            print()
          else:
            alimento
            if alimento in alimentos:
              while True:
                try:
                  quantidade = float(input("Quantidade a ser removida:"))
                  print()
                  break
                except ValueError:
                  print("Insira uma quantidade válida")
                  print()
              if alimento in alimentos:
                if alimentos[alimento] >= quantidade:
                  alimentos[alimento] -= quantidade
                  if alimentos[alimento] == 0:
                    del alimentos[alimento]
                else:
                  print("Quantidade insuficiente na despensa")
                  print()
            else:
              print("Alimento não encontrado na despensa")
              print()
        os.system("clear")
        exibir_alimentos()
        print()
        input("<ENTER> para voltar")

      elif opLista == "3":
        os.system("clear")
        exibir_alimentos()
        print()
        input("<ENTER> para voltar")

  elif menu == "3":
    opLista = " "
    while opLista != "0":
      os.system("clear")
      print()
      print("+--------------------+")
      print("|     Bebidas        |")
      print("+--------------------+")
      print("| 1 - Adicionar      |")
      print("| 2 - Remover        |")
      print("| 3 - Exibir         |")
      print("| 0 - Voltar ao MENU |")
      print("+--------------------+")
      opLista = input("| Escolha uma opção:")

      if opLista == "1":
        os.system("clear")
        while True:
          print("Digite 'SAIR' para voltar")
          print()
          exibir_bebidas()
          bebida = input("Adicionar Bebida:")
          if bebida.upper() == "SAIR":
            break
          elif bebida.isdigit():
            print("Insira um nome válido")
            print()
          elif bebida.strip() == '':
            print("Insira um nome válido")
            print()
          else:
            bebida
            while True:
              try:
                quantidade = float(input("Quantidade a ser adicionada:"))
                print()
                break
              except ValueError:
                print("Insira uma quantidade válida")
                print()
            if bebida in bebidas:
              bebidas[bebida] += quantidade
            else:
              bebidas[bebida] = quantidade
        os.system("clear")
        exibir_bebidas()
        print()
        input("<ENTER> para voltar")

      elif opLista == "2":
        os.system("clear")
        print("Digite 'SAIR' para voltar")
        print()
        while True:
          print("Digite 'SAIR' para voltar")
          print()
          exibir_bebidas()
          bebida = input("Remover Bebida:")
          if bebida.upper() == "SAIR":
            break
          elif bebida.isdigit():
            print("Insira um nome válido")
            print()
          elif bebida.strip() == '':
            print("Insira um nome válido")
            print()
          else:
            bebida
            if bebida in bebidas:
              while True:
                try:
                  quantidade = float(input("Quantidade a ser removida:"))
                  print()
                  break
                except ValueError:
                  print("Insira uma quantidade válida")
                  print()
              if bebida in bebidas:
                if bebidas[bebida] >= quantidade:
                  bebidas[bebida] -= quantidade
                  if bebidas[bebida] == 0:
                    del bebidas[bebida]
                else:
                  print("Quantidade insuficiente na despensa")
                  print()
            else:
              print("Bebida não encontrada na despensa")
              print()
        os.system("clear")
        exibir_bebidas()
        print()
        input("<ENTER> para voltar")

      elif opLista == "3":
        os.system("clear")
        exibir_bebidas()
        print()
        input("<ENTER> para voltar")

  elif menu == "4":
    opLista = " "
    while opLista != "0":
      os.system("clear")
      print()
      print("+--------------------+")
      print("|  Higiene Pessoal   |")
      print("+--------------------+")
      print("| 1 - Adicionar      |")
      print("| 2 - Remover        |")
      print("| 3 - Exibir         |")
      print("| 0 - Voltar ao MENU |")
      print("+--------------------+")
      opLista = input("| Escolha uma opção:")

      if opLista == "1":
        os.system("clear")
        while True:
          print("Digite 'SAIR' para voltar")
          print()
          exibir_hpessoals()
          hpessoal = input("Adicionar Produto de Higiene Pessoal:")
          if hpessoal.upper() == "SAIR":
            break
          elif hpessoal.isdigit():
            print("Insira um nome válido")
            print()
          elif hpessoal.strip() == '':
            print("Insira um nome válido")
            print()
          else:
            hpessoal
            while True:
              try:
                quantidade = float(input("Quantidade a ser adicionada:"))
                print()
                break
              except ValueError:
                print("Insira uma quantidade válida")
                print()
            if hpessoal in hpessoals:
              hpessoals[hpessoal] += quantidade
            else:
              hpessoals[hpessoal] = quantidade
        os.system("clear")
        exibir_hpessoals()
        print()
        input("<ENTER> para voltar")

      elif opLista == "2":
        os.system("clear")
        while True:
          print("Digite 'SAIR' para voltar")
          print()
          exibir_hpessoals()
          hpessoal = input("Remover Produto de Higiene Pessoal:")
          if hpessoal.upper() == "SAIR":
            break
          elif hpessoal.isdigit():
            print("Insira um nome válido")
            print()
          elif hpessoal.strip() == '':
            print("Insira um nome válido")
            print()
          else:
            hpessoal
            if hpessoal in hpessoals:
              while True:
                try:
                  quantidade = float(input("Quantidade a ser removida:"))
                  print()
                  break
                except ValueError:
                  print("Insira uma quantidade válida")
                  print()
              if hpessoal in hpessoals:
                if hpessoals[hpessoal] >= quantidade:
                  hpessoals[hpessoal] -= quantidade
                  if hpessoals[hpessoal] == 0:
                    del hpessoals[hpessoal]
                else:
                  print("Quantidade insuficiente na despensa")
                  print()
            else:
              print("Produto não encontrado na despensa")
              print()
        os.system("clear")
        exibir_hpessoals()
        print()
        input("<ENTER> para voltar")

      elif opLista == "3":
        os.system("clear")
        exibir_hpessoals()
        print()
        input("<ENTER> para voltar")

  elif menu == "5":
    opLista = " "
    while opLista != "0":
      os.system("clear")
      print()
      print("+-----------------------+")
      print("|  Produtos de Limpeza  |")
      print("+-----------------------+")
      print("| 1 - Adicionar         |")
      print("| 2 - Remover           |")
      print("| 3 - Exibir            |")
      print("| 0 - Voltar ao MENU    |")
      print("+-----------------------+")
      opLista = input("| Escolha uma opção:")

      if opLista == "1":
        os.system("clear")
        while True:
          print("Digite 'SAIR' para voltar")
          print()
          exibir_plimpezas()
          plimpeza = input("Adicionar Produto de Limpeza:")
          if plimpeza.upper() == "SAIR":
            break
          elif plimpeza.isdigit():
            print("Insira um nome válido")
            print()
          elif plimpeza.strip() == '':
            print("Insira um nome válido")
            print()
          else:
            plimpeza
            while True:
              try:
                quantidade = float(input("Quantidade a ser adicionada:"))
                print()
                break
              except ValueError:
                print("Insira uma quantidade válida")
                print()
            if plimpeza in plimpezas:
              plimpezas[plimpeza] += quantidade
            else:
              plimpezas[plimpeza] = quantidade
        os.system("clear")
        exibir_plimpezas()
        print()
        input("<ENTER> para voltar")

      elif opLista == "2":
        os.system("clear")
        while True:
          print("Digite 'SAIR' para voltar")
          print()
          exibir_plimpezas()
          plimpeza = input("Remover Produto de Limpeza:")
          if plimpeza.upper() == "SAIR":
            break
          elif plimpeza.isdigit():
            print("Insira um nome válido")
            print()
          elif plimpeza.strip() == '':
            print("Insira um nome válido")
            print()
          else:
            plimpeza
            if plimpeza in plimpezas:
              while True:
                try:
                  quantidade = float(input("Quantidade a ser removida:"))
                  print()
                  break
                except ValueError:
                  print("Insira uma quantidade válida")
                  print()
              if plimpeza in plimpezas:
                if plimpezas[plimpeza] >= quantidade:
                  plimpezas[plimpeza] -= quantidade
                  if plimpezas[plimpeza] == 0:
                    del plimpezas[plimpeza]
                else:
                  print("Quantidade insuficiente na despensa")
                  print()
            else:
              print("Produto não encontrado na despensa")
              print()
        os.system("clear")
        exibir_plimpezas()
        print()
        input("<ENTER> para voltar")

      elif opLista == "3":
        os.system("clear")
        exibir_plimpezas()
        print()
        input("<ENTER> para voltar")

  elif menu == "6":
    opLista = " "
    while opLista != "0":
      os.system("clear")
      print()
      print("+----------------------+")
      print("|     Ferramentas      |")
      print("+----------------------+")
      print("| 1 - Adicionar        |")
      print("| 2 - Remover          |")
      print("| 3 - Exibir           |")
      print("| 0 - Voltar ao MENU   |")
      print("+----------------------+")
      opLista = input("|Escolha uma opção:")

      if opLista == "1":
        os.system("clear")
        while True:
          print("Digite 'SAIR' para voltar")
          print()
          exibir_ferramentas()
          ferramenta = input("Adicionar Produto de Limpeza:")
          if ferramenta.upper() == "SAIR":
            break
          elif ferramenta.isdigit():
            print("Insira um nome válido")
            print()
          elif ferramenta.strip() == '':
            print("Insira um nome válido")
            print()
          else:
            ferramenta
            while True:
              try:
                quantidade = float(input("Quantidade a ser adicionada:"))
                print()
                break
              except ValueError:
                print("Insira uma quantidade válida")
                print()
            if ferramenta in ferramentas:
              ferramentas[ferramenta] += quantidade
            else:
              ferramentas[ferramenta] = quantidade
        os.system("clear")
        exibir_ferramentas()
        print()
        input("<ENTER> para voltar")

      elif opLista == "2":
        os.system("clear")
        while True:
          print("Digite 'SAIR' para voltar")
          print()
          exibir_ferramentas()
          ferramenta = input("Remover Ferramenta:")
          if ferramenta.upper() == "SAIR":
            break
          elif ferramenta.isdigit():
            print("Insira um nome válido")
            print()
          elif ferramenta.strip() == '':
            print("Insira um nome válido")
            print()
          else:
            ferramenta
            if ferramenta in ferramentas:
              while True:
                try:
                  quantidade = float(input("Quantidade a ser removida:"))
                  print()
                  break
                except ValueError:
                  print("Insira uma quantidade válida")
                  print()
              if ferramenta in ferramentas:
                if ferramentas[ferramenta] >= quantidade:
                  ferramentas[ferramenta] -= quantidade
                  if ferramentas[ferramenta] == 0:
                    del ferramentas[ferramenta]
                else:
                  print("Quantidade insuficiente na despensa")
                  print()
            else:
              print("Ferramenta não encontrado na despensa")
              print()
        os.system("clear")
        exibir_ferramentas()
        print()
        input("<ENTER> para voltar")

      elif opLista == "3":
        os.system("clear")
        exibir_ferramentas()
        print()
        input("<ENTER> para voltar")

print("Programa Encerrado")

#-Salvando os dicionários em arquivos, pelo pickle------------------------------

arq_alimentos = open("arq_alimentos.dat", "wb")
pickle.dump(alimentos, arq_alimentos)
arq_alimentos.close()

arq_bebidas = open("arq_bebidas.dat", "wb")
pickle.dump(bebidas, arq_bebidas)
arq_bebidas.close()

arq_hpessoals = open("arq_hpessoals.dat", "wb")
pickle.dump(hpessoals, arq_hpessoals)
arq_hpessoals.close()

arq_plimpezas = open("arq_plimpezas.dat", "wb")
pickle.dump(plimpezas, arq_plimpezas)
arq_plimpezas.close()

arq_ferramentas = open("arq_ferramentas.dat", "wb")
pickle.dump(ferramentas, arq_ferramentas)
arq_ferramentas.close()