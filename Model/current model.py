import os

#####################################
##### Projeto Escola - Versão 6 #####
#####################################

alunos = {
    '123' : ["Allysson Dantas", "allyson@ufrn.br", "99999-9999"],
    '456' : ["Geocasta Souza", "geo@ufrn.br", "88888-8888"],
    '789' : ["Vitória Pereira", "vivi@ufrn.br", "77777-7777"]
}

professores = {}

turmas = {}

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
  print("Aluno cadastrado com sucesso!")
  input("Tecle <ENTER> para continuar...")


def exibir_aluno():
  os.system('clear')
  print()
  print("############################################")
  print("#####        Exibe Dados do Aluno      #####")
  print("############################################")
  print()
  matr = input("Qual a matrícula do aluno: ")
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
  matr = input("Qual a matrícula do aluno: ")
  if matr in alunos:
      print("Informe os novos dados do aluno: ")
      nome = input("##### Nome: ")
      print()
      email = input("##### Email: ")
      print()
      fone = input("##### Celular: ")
      print()
      alunos[matr] = [nome, email, fone]
      print("Aluno alterado com sucesso!")
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
  matr = input("Qual a matrícula do(a) aluno(a): ")
  if matr in alunos:
      print("Nome:", alunos[matr][0])
      print("E-mail:", alunos[matr][1])
      print("Fone:", alunos[matr][2])
      print()
      resp = input("Tem certeza que deseja excluir o aluno [S/N]? ")
      if resp == 'S' or resp == 's':
        del alunos[matr]
        print("Aluno(a) excluído(a) com sucesso!")
      else:
        print("Exclusão não realizada!")
  else:
      print("Aluno(a) inexistente!")
  input("Tecle <ENTER> para continuar...")


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
        print()
        print("############################################")
        print("#####         Módulo Professor         #####")
        print("############################################")
        print("##### 1 - Cadastrar Professor          #####")
        print("##### 2 - Exibir Dados do Professor    #####")
        print("##### 3 - Alterar Dados do Professor   #####")
        print("##### 4 - Excluir Professor            #####")
        print("##### 0 - Retornar ao Menu Principal   #####")
        op_aluno = input("##### Escolha sua opção: ")
        print()
        input("Tecle <ENTER> para continuar...")
    elif op_princ == '3':
        print()
        print("############################################")
        print("#####           Módulo Turma           #####")
        print("############################################")
        print("##### 1 - Cadastrar Turma              #####")
        print("##### 2 - Exibir Dados da Turma        #####")
        print("##### 3 - Alterar Dados da Turma       #####")
        print("##### 4 - Excluir Turma                #####")
        print("##### 0 - Retornar ao Menu Principal   #####")
        op_aluno = input("##### Escolha sua opção: ")
        print()
        input("Tecle <ENTER> para continuar...")
    elif op_princ == '4':
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
        op_aluno = input("##### Escolha sua opção: ")
        print()
        input("Tecle <ENTER> para continuar...")
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
