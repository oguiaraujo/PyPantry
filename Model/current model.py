import os
import pickle

#####################################
##### Projeto Escola - Versão 11 ####
#####################################

alunos = {}
try:
  arq_alunos = open("alunos.dat", "rb")
  alunos = pickle.load(arq_alunos)
except:
  arq_alunos = open("alunos.dat", "wb")
arq_alunos.close()


professores = {}
try:
  arq_profs = open("professores.dat", "rb")
  professores = pickle.load(arq_profs)

except:
  arq_profs = open("professores.dat", "wb")
arq_profs.close()

turmas = {}
try:
  arq_turmas = open("turmas.dat", "rb")
  turmas = pickle.load(arq_turmas)
except:
  arq_turmas = open("turmas.dat", "wb")
arq_turmas.close()



################################################################
################################################################
##########               F U N Ç Õ E S                ##########
################################################################
################################################################

def menu_principal():
  os.system('clear')
  print("############################################")
  print("######       Projeto SIG-Escola       ######")
  print("############################################")
  print("#####      1 - Módulo Aluno            #####")
  print("#####      2 - Módulo Professor        #####")
  print("#####      3 - Módulo Turma            #####")
  print("#####      4 - Módulo Relatório        #####")
  print("#####      5 - Módulo Informações      #####")
  print("#####      0 - Sair                    #####")
  op_princ = input("##### Escolha sua opção: ")
  return op_princ


def menu_aluno():
  os.system('clear')
  print()
  print("############################################")
  print("#####           Módulo Aluno           #####")
  print("############################################")
  print("##### 1 - Cadastrar Aluno              #####")
  print("##### 2 - Exibir Dados do Aluno        #####")
  print("##### 3 - Alterar Dados do Aluno       #####")
  print("##### 4 - Excluir Aluno                #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  op_aluno = input("##### Escolha sua opção: ")
  return op_aluno
  

def cadastrar_aluno():
  os.system('clear')
  print()
  print("############################################")
  print("#####           Cadastra Aluno         #####")
  print("############################################")
  print()
  nome = input("##### Nome: ")
  print()
  matr = input("##### Matrícula: ")
  print()
  email = input("##### Email: ")
  print()
  fone = input("##### Celular: ")
  print()
  alunos[matr] = [nome, email, fone]
  print(alunos)
  print("Aluno(a) cadastrado(a) com sucesso!")
  input("Tecle <ENTER> para continuar...")


def exibir_aluno():
  os.system('clear')
  print()
  print("############################################")
  print("#####        Exibe Dados do Aluno      #####")
  print("############################################")
  print()
  matr = input("Qual a matrícula do(a) aluno(a)? ")
  if matr in alunos:
    print("##### Nome: ", alunos[matr][0])
    print("##### Matrícula: ", matr)
    print("##### Email: ", alunos[matr][1])
    print("##### Celular: ", alunos[matr][2])
  else:
    print("Aluno(a) inexistente!")
  print()
  input("Tecle <ENTER> para continuar...")


def alterar_aluno():
  os.system('clear')
  print()
  print("############################################")
  print("#####       Altera Dados do Aluno      #####")
  print("############################################")
  print()
  matr = input("Qual a matrícula do(a) aluno(a)? ")
  if matr in alunos:
    print("Informe os novos dados do(a) aluno(a): ")
    nome = input("##### Nome: ")
    print()
    email = input("##### Email: ")
    print()
    fone = input("##### Celular: ")
    print()
    alunos[matr] = [nome, email, fone]
    print("Aluno(a) alterado(a) com sucesso!")
  else:
    print("Aluno(a) inexistente!")
  input("Tecle <ENTER> para continuar...")


def excluir_aluno():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Exclui Aluno             #####")
  print("############################################")
  print()
  matr = input("Qual a matrícula do(a) aluno(a)? ")
  if matr in alunos:
    print("Nome:", alunos[matr][0])
    print("E-mail:", alunos[matr][1])
    print("Fone:", alunos[matr][2])
    print()
    resp = input("Tem certeza que deseja excluir o(a) aluno(a) [S/N]? ")
    if resp == 'S' or resp == 's':
      del alunos[matr]
      print("Aluno(a) excluído(a) com sucesso!")
    else:
      print("Exclusão não realizada!")
  else:
    print("Aluno(a) inexistente!")
  input("Tecle <ENTER> para continuar...")



  
def menu_prof():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Módulo Professor         #####")
  print("############################################")
  print("##### 1 - Cadastrar Professor          #####")
  print("##### 2 - Exibir Dados do Professor    #####")
  print("##### 3 - Alterar Dados do Professor   #####")
  print("##### 4 - Excluir Professor            #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  op_prof = input("##### Escolha sua opção: ")
  return op_prof


def cadastrar_prof():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Cadastra Professor       #####")
  print("############################################")
  print()
  nome = input("##### Nome: ")
  print()
  cpf = input("##### CPF: ")
  print()
  email = input("##### Email: ")
  print()
  fone = input("##### Celular: ")
  print()
  professores[cpf] = [nome, email, fone]
  print(professores)
  print("Professor(a) cadastrado(a) com sucesso!")
  input("Tecle <ENTER> para continuar...")


def exibir_prof():
  os.system('clear')
  print()
  print("############################################")
  print("#####      Exibe Dados do Professor    #####")
  print("############################################")
  print()
  cpf = input("Qual o CPF do(a) professor(a)? ")
  if cpf in professores:
    print("##### Nome   : ", professores[cpf][0])
    print("##### CPF    : ", cpf)
    print("##### Email  : ", professores[cpf][1])
    print("##### Celular: ", professores[cpf][2])
  else:
    print("Professor(a) inexistente!")
  print()
  input("Tecle <ENTER> para continuar...")


def alterar_prof():
  os.system('clear')
  print()
  print("############################################")
  print("#####     Altera Dados do Professor    #####")
  print("############################################")
  print()
  cpf = input("Qual o CPF do(a) professor(a)? ")
  if cpf in professores:
    print("Informe os novos dados do(a) professor(a): ")
    nome = input("##### Nome: ")
    print()
    email = input("##### Email: ")
    print()
    fone = input("##### Celular: ")
    print()
    professores[cpf] = [nome, email, fone]
    print("Professor(a) alterado(a) com sucesso!")
  else:
    print("Professor(a) inexistente!")
  input("Tecle <ENTER> para continuar...")


def excluir_prof():
  os.system('clear')
  print()
  print("############################################")
  print("#####       Exclui Professor           #####")
  print("############################################")
  print()
  cpf = input("Qual o CPF do(a) professor(a)? ")
  if cpf in professores:
    print("Nome:", professores[cpf][0])
    print("E-mail:", professores[cpf][1])
    print("Fone:", professores[cpf][2])
    print()
    resp = input("Tem certeza que deseja excluir o(a) professor(a) [S/N]? ")
    if resp == 'S' or resp == 's':
      del professores[cpf]
      print("Professor(a) excluído(a) com sucesso!")
    else:
      print("Exclusão não realizada!")
  else:
    print("Professor(a) inexistente!")
  input("Tecle <ENTER> para continuar...")




def menu_turma():
  os.system('clear')
  print()
  print("############################################")
  print("#####           Módulo Turma           #####")
  print("############################################")
  print("##### 1 - Cadastrar Turma              #####")
  print("##### 2 - Exibir Dados da Turma        #####")
  print("##### 3 - Alterar Dados da Turma       #####")
  print("##### 4 - Excluir Turma                #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  op_turma = input("##### Escolha sua opção: ")
  return op_turma


def cadastrar_turma():
  os.system('clear')
  print()
  print("############################################")
  print("#####           Cadastra Turma         #####")
  print("############################################")
  print()
  cod = input("##### Código da Turma: ")
  print()
  nome = input("##### Nome da Turma: ")
  print()
  horario = input("##### Horário: ")
  print()
  sala = input("##### Sala: ")
  print()
  cpf = input("##### CPF do Professor: ")
  print()
  turmas[cod] = [nome, horario, sala, cpf]
  print(turmas)
  print("Turma cadastrada com sucesso!")
  input("Tecle <ENTER> para continuar...")


def exibir_turma():
  os.system('clear')
  print()
  print("############################################")
  print("#####        Exibe Dados da Turma      #####")
  print("############################################")
  print()
  cod = input("Informe o código da turma: ")
  if cod in turmas:
    print("##### Código       : ", cod)
    print("##### Nome da Turma: ", turmas[cod][0])
    print("##### Horário      : ", turmas[cod][1])
    print("##### Sala de Aula : ", turmas[cod][2])
    print("##### Professor(a) : ", turmas[cod][3])
  else:
    print("Turma(a) inexistente!")
  print()
  input("Tecle <ENTER> para continuar...")


def alterar_turma():
  os.system('clear')
  print()
  print("############################################")
  print("#####       Altera Dados da Turma      #####")
  print("############################################")
  print()
  cod = input("Qual o código da turma? ")
  if cod in turmas:
    print("Informe os novos dados da turma: ")
    print()
    cod = input("##### Código da Turma: ")
    print()
    nome = input("##### Nome da Turma: ")
    print()
    horario = input("##### Horário: ")
    print()
    sala = input("##### Sala: ")
    print()
    cpf = input("##### CPF do Professor: ")
    print()
    turmas[cod] = [nome, horario, sala, cpf]
    print("Turma alterada com sucesso!")
  else:
    print("Turma inexistente!")
  input("Tecle <ENTER> para continuar...")


def excluir_turma():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Exclui Turma             #####")
  print("############################################")
  print()
  cod = input("Qual o código da turma ")
  if cod in turmas:
    print("##### Nome da Turma: ", turmas[cod][0])
    print("##### Horário      : ", turmas[cod][1])
    print("##### Sala de Aula : ", turmas[cod][2])
    print("##### Professor(a) : ", turmas[cod][3])
    print()
    resp = input("Tem certeza que deseja excluir a turma [S/N]? ")
    if resp == 'S' or resp == 's':
      del turmas[cod]
      print("Aluno(a) excluído(a) com sucesso!")
    else:
      print("Exclusão não realizada!")
  else:
    print("Aluno(a) inexistente!")
  input("Tecle <ENTER> para continuar...")




def menu_relat():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Módulo Relatório         #####")
  print("############################################")
  print("##### 1 - Lista Geral de Alunos        #####")
  print("##### 2 - Lista Geral de Professores   #####")
  print("##### 3 - Lista Geral de Turmas        #####")
  print("##### 4 - Lista de Alunos por Turma    #####")
  print("##### 5 - Lista de Turmas p/ Professor #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  op_relat = input("##### Escolha sua opção: ")
  return op_relat

def lista_geral_alunos():
  os.system('clear')
  print()
  print("##################################################################################")
  print("#######################      Relatório Geral de Alunos     #######################")
  print("##################################################################################")
  print("|-----------|-----------------------------|--------------------|-----------------|")
  print("| Matrícula |        Nome Completo        |       E-mail       |     Celular     |")
  print("|-----------|-----------------------------|--------------------|-----------------|")
  for matr in alunos:
    print("| %-9s "%(matr), end='')
    print("| %-27s "%(alunos[matr][0]), end='')
    print("| %-18s "%(alunos[matr][1]), end='')
    print("| %-15s |"%(alunos[matr][2]))
  print("|-----------|-----------------------------|--------------------|-----------------|")
  print()
  input("Tecle <ENTER> para continuar...")


def lista_geral_profs():
  os.system('clear')
  print()
  print("##################################################################################")
  print("#######################   Relatório Geral de Professores   #######################")
  print("##################################################################################")
  print("|-------------|---------------------------|--------------------|-----------------|")
  print("|     CPF     |       Nome Completo       |       E-mail       |     Celular     |")
  print("|-------------|---------------------------|--------------------|-----------------|")
  for cpf in professores:
    print("| %-11s "%(cpf), end='')
    print("| %-25s "%(professores[cpf][0]), end='')
    print("| %-18s "%(professores[cpf][1]), end='')
    print("| %-15s |"%(professores[cpf][2]))
  print("|-------------|---------------------------|--------------------|-----------------|")
  print()
  input("Tecle <ENTER> para continuar...")


def lista_geral_turmas():
  os.system('clear')
  print()
  print("##################################################################################")
  print("#######################      Relatório Geral de Turmas     #######################")
  print("##################################################################################")
  print("|------------|----------------------------------------|-------------|------------|")
  print("|   Código   |              Nome da Turma             |   Horário   |    Sala    |")
  print("|------------|----------------------------------------|-------------|------------|")
  for cod in turmas:
    print("| %-10s "%(cod), end='')
    print("| %-38s "%(turmas[cod][0]), end='')
    print("| %-11s "%(turmas[cod][1]), end='')
    print("| %-10s |"%(turmas[cod][2]))
  print("|------------|----------------------------------------|-------------|------------|")
  #turmas[cod] = [nome, horario, sala, cpf]
  print()
  input("Tecle <ENTER> para continuar...")


def lista_alunos_turma():
  os.system('clear')
  print()
  print("##################################################################################")
  print("#######################    Relatório de Alunos por Turma   #######################")
  print("##################################################################################")
  print()
  input("Tecle <ENTER> para continuar...")


def lista_turmas_prof():
  os.system('clear')
  print()
  cpf = input("Qual o CPF do(a) professor(a)? ")
  if cpf in professores:
    nome_prof = professores[cpf][0]
    print("##################################################################################")
    print("#######################  Relatório de Turmas por Professor #######################")
    print("##################################################################################")
    print("#######################  Professor(a): %-19s #######################"%nome_prof)
    print("##################################################################################")
    print("|------------|----------------------------------------|-------------|------------|")
    print("|   Código   |              Nome da Turma             |   Horário   |    Sala    |")
    print("|------------|----------------------------------------|-------------|------------|")
    for cod in turmas:
      if turmas[cod][3] == cpf:
        print("| %-10s "%(cod), end='')
        print("| %-38s "%(turmas[cod][0]), end='')
        print("| %-11s "%(turmas[cod][1]), end='')
        print("| %-10s |"%(turmas[cod][2]))
    print("|------------|----------------------------------------|-------------|------------|")
  else:
    print("Professor(a) inexistente!")
  print()
  input("Tecle <ENTER> para continuar...")


# lista_geral_alunos()
# input()
################################################################
################################################################
##########    P R O G R A M A   P R I N C I P A L     ##########
################################################################
################################################################

op_princ = ''
while op_princ != '0':
  op_princ = menu_principal()

  if op_princ == '1':
    op_aluno = ''
    while op_aluno != '0':
      op_aluno = menu_aluno()
      print()
      if op_aluno == '1':
          cadastrar_aluno()
      elif op_aluno == '2':
          exibir_aluno()
      elif op_aluno == '3':
          alterar_aluno()
      elif op_aluno == '4':
          excluir_aluno()
            
  elif op_princ == '2':
    op_prof = ''
    while op_prof != '0':
      op_prof = menu_prof()
      print()
      if op_prof == '1':
          cadastrar_prof()
      elif op_prof == '2':
          exibir_prof()
      elif op_prof == '3':
          alterar_prof()
      elif op_prof == '4':
          excluir_prof()
    
  elif op_princ == '3':
    op_turma = ''
    while op_turma != '0':
      op_turma = menu_turma()
      print()
      if op_turma == '1':
          cadastrar_turma()
      elif op_turma == '2':
          exibir_turma()
      elif op_turma == '3':
          alterar_turma()
      elif op_turma == '4':
          excluir_turma()
        
  elif op_princ == '4':


    op_relat = ''
    while op_relat != '0':
      op_relat = menu_relat()
      print()
      if op_relat == '1':
          lista_geral_alunos()
      elif op_relat == '2':
          lista_geral_profs()
      elif op_relat == '3':
          lista_geral_turmas()
      elif op_relat == '4':
          lista_alunos_turma()
      elif op_relat == '5':
          lista_turmas_prof()
  
  elif op_princ == '5':
    print()
    print("############################################")
    print("#####  Você está no Módulo Informações  ####")
    print("############################################")
    print()
    print("##### Projeto de Gestão de uma Escola   ####")
    print("##### Equipe de desenvolvimento:        ####")
    print("##### Flavius Gorgônio @flgorgonio      ####")
    print("##### © Copyright by UFRN, since 2023   ####")
    print("##### Licença Pública Geral GNU         ####")
    print("##### www.gnu.org/licenses/gpl.html     ####")
    print()
    input("Tecle <ENTER> para continuar...")


print("Você encerrou o programa!")
print("Até logo!")

### Gravando os dados no arquivo

arq_alunos = open("alunos.dat", "wb")
pickle.dump(alunos, arq_alunos)
arq_alunos.close()

arq_profs = open("professores.dat", "wb")
pickle.dump(professores, arq_profs)
arq_profs.close()


arq_turmas = open("turmas.dat", "wb")
pickle.dump(turmas, arq_turmas)
arq_turmas.close()