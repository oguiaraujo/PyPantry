from datetime import datetime

#Adaptado do chatGPT
def gera_cod(itens):
  cod = len(itens) + 1
  print("|")
  print("\033[92m| Código do item:", cod,"\033[0m") #Alteração de cor, tirada do chatGPT
  print("|")
  return cod


def gera_data_hora():
   dt_hr = datetime.now()
   dt_hr = dt_hr.strftime('%d%m%Y%H%M%S')
   print("\033[92m| Código por data e hora:", dt_hr,"\033[0m")
   print("|")
   return dt_hr


def erro_cod():
    print("| Este código não pertence a nenhum CADASTRO AQUI!")
    print()
    input("<ENTER> para continuar")


def removido():
    print("| REMOÇÃO bem sucedida!")
    print()
    input("<ENTER> para continuar")


def cadastrado():
    print("| CADASTRO bem sucedido!")
    print()
    input("<ENTER> para continuar")


def alterado():
    print("| ALTERAÇÃO bem sucedida!")
    print()
    input("<ENTER> para continuar")
