import os
from modulos import menus_opcoes, func_itens, func_comp, func_ret, func_estoque, func_list_comp, func_relatorios
import pickle


#-Criando/Abrindo arquivos binários com pickle
itens = {}
try:
  arq_itens = open("itens.dat", "rb")
  itens = pickle.load(arq_itens)
except:
  arq_itens = open("itens.dat", "wb")
arq_itens.close()

compras = {}
try:
  arq_compras= open("compras.dat", "rb")
  compras = pickle.load(arq_compras)
except:
  arq_compras = open("compras.dat", "wb")
arq_compras.close()

retiradas = {}
try:
  arq_retiradas = open("retiradas.dat", "rb")
  retiradas = pickle.load(arq_retiradas)
except:
  arq_retiradas = open("retiradas.dat", "wb")
arq_retiradas.close()

estoque = {}
try:
  arq_estoque = open("estoque.dat", "rb")
  estoque = pickle.load(arq_estoque)
except:
  arq_estoque = open("estoque.dat", "wb")
arq_estoque.close()


# Programa principal 
op_menu = ""
while op_menu != "0":
  op_menu = menus_opcoes.menu_pypantry()
  
  if op_menu == "1":
    op_itens = ""
    while op_itens != "0":
      op_itens = menus_opcoes.menu_itens()
      if op_itens == "1":
        func_itens.cadastra_item(itens)
      elif op_itens == "2":
        func_itens.exibe_item(itens)
      elif op_itens == "3":
        func_itens.altera_item(itens)
      elif op_itens == "4":
        func_itens.remove_item(itens, estoque)

  elif op_menu == "2":
    op_compras = ""
    while op_compras != "0":
      op_compras = menus_opcoes.menu_compras()
      if op_compras == "1":
        func_comp.cadastra_compra(compras, itens, estoque)
      elif op_compras == "2":
        func_comp.exibe_compra(compras, itens)
      elif op_compras == "3":
        func_comp.altera_compra(compras, estoque)
      elif op_compras == "4":
        func_comp.remove_compra(compras, itens, estoque)

  elif op_menu == "3":
    op_retiradas = ""
    while op_retiradas != "0":
        op_retiradas = menus_opcoes.menu_retiradas()
        if op_retiradas == "1":
          func_ret.cadastra_retirada(retiradas, itens, estoque)
        elif op_retiradas == "2":
          func_ret.exibe_retirada(retiradas, itens)
        elif op_retiradas == "3":
          func_ret.altera_retirada(retiradas, estoque)
        elif op_retiradas == "4":
          func_ret.remover_retirada(compras, itens, estoque)
        
  elif op_menu == "4":
    menus_opcoes.estoque()
    func_estoque.exibe_estoque(estoque, itens)

  elif op_menu == "5":
    menus_opcoes.lista_de_compras()
    func_list_comp.exibe_lista_de_compras(estoque, itens)

  elif op_menu == "6":
    op_relatorios = ""
    while op_relatorios != "0":
      op_relatorios = menus_opcoes.relatorios()
      if op_relatorios == "1":
        func_relatorios.exibe_todos_itens(itens)
      elif op_relatorios == "2":
        func_relatorios.exibe_itens_por_categoria(itens)
      elif op_relatorios == "3":
        func_relatorios.exibe_itens_por_marca(itens)
      elif op_relatorios == "4":
        func_relatorios.exibe_todas_compras(compras, itens)
      elif op_relatorios == "5":
        func_relatorios.exibe_compras_por_data(compras, itens)
      elif op_relatorios == "6":
        func_relatorios.exibe_todas_retiradas(retiradas, itens)
      elif op_relatorios == "7":
        func_relatorios.exibe_retiradas_por_data(retiradas, itens)
    
  elif op_menu == "7":
    os.system('clear')
    print()
    print("+--------------------------------------+")
    print("|              INFORMAÇÕES             |")
    print("|               PYPANTRY               |")
    print("+--------------------------------------+")
    print("| Projeto de Controle de Despensa      |")
    print("| Desenvolvedor: Guilherme Araújo      |")
    print("| GitHub: oguiaraujo                   |")
    print("| Replit: oguiaraujo                   |")
    print("| Instagram: somuliro                  |")
    print("+--------------------------------------+")
    print()
    input("| <ENTER> para voltar")

#-Salvando os dados em seus respectivos arquivos binários-----------------------
arq_itens = open("itens.dat", "wb")
pickle.dump(itens, arq_itens)
arq_itens.close()

arq_compras = open("compras.dat", "wb")
pickle.dump(compras, arq_compras)
arq_compras.close()

arq_retiradas = open("retiradas.dat", "wb")
pickle.dump(retiradas, arq_retiradas)
arq_retiradas.close()

arq_estoque = open("estoque.dat", "wb")
pickle.dump(estoque, arq_estoque)
arq_estoque.close()

print("PyPantry encerrado!")