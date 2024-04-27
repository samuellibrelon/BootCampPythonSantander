# Projeto 1 Python Básico - BootCamp Python Vivo
# bankSystem.py - Otimizando o Sistema bancário com funções em Python

QTD_SAQUE = 0
QTD_DEPOSITO = 0
saldo = 0
numeroConta = 0
usuarios = []

def main(): #função principal 
  while True:
    opcao = showMenu()
    if opcao not in ['d', 's', 'e', 'x', 'c', 'b', 'l']: #verifica input
      print('Opção inválida!')
      continue
    if opcao == 'd':
      print('Digite o valor do depósito: ')
      valorDeposito = float(input())
      realizarDeposito(valorDeposito)
    elif opcao == 'e':
      emitirExtrato()
    elif opcao == 's':
      print('Digite o valor do saque: ')
      valorSaque = float(input())
      realizarSaque(valorSaque)
    elif opcao == 'c':
      cadastrarUsuario()
    elif opcao == 'b':
      cadastarContaBancaria(cadastrarUsuario)
    elif opcao == 'l':
      listarContas()
    elif opcao == 'x':
      break

def realizarDeposito(valorDeposito): #realiza o depósito
  global  saldo, QTD_DEPOSITO
  if valorDeposito > 0: #verifica se o valor é positivo
    saldo += valorDeposito
    QTD_DEPOSITO += 1
    print('Depósito realizado com sucesso')
  else:
    print('O valor precisa ser positivo')
    
def realizarSaque(valorSaque): #realiza o saque
  global saldo, QTD_SAQUE
  if QTD_SAQUE < 3: #verifica se excedeu o valor máximo de saques
    if  0 < valorSaque <= 500.00: #verifica se é um valor entre 0 e 501
      saldo -= valorSaque
      QTD_SAQUE += 1
      print('Saque realizado com sucesso')
    else:
      print('O valor do saque deve ser entre 1 e R$500.00')
  else:
    print('Você excedeu o valor de saques diários')

def emitirExtrato(): #emite o extrato
  global saldo, QTD_DEPOSITO, QTD_SAQUE
  print('''
  Saldo: R${:.2f}
  Depósitos realizados: {}
  Saques realizados: {}
  '''.format(saldo, QTD_DEPOSITO, QTD_SAQUE))

def showMenu(): #exibe o menu e retorna a opção escolhida
  MENU = '''
  ============MENU============
  |                          |
  | d = Depósito             |
  | c = cadastrar cliente    |
  | b = cadastar conta banc  |
  | s = Saque                |
  | e = Extrato              |
  | x = sair                 |
  | l = listar contas       |
  |                          |
  ===========================
  '''
  print (MENU + '\nOpção: ')
  opcao = str(input().lower())
  return opcao

def cadastrarUsuario(): #cadastra o usuário e as suas informações pessoais
  print('Digite o seu nome')
  nome = str(input())
  print('Digite a sua data de nascimento(ex: 20/06/1998): ')
  dataNascimento = str(input())
  print('Digite o seu CPF: ')
  cpf = int(input())
  print('Digite o seu endereço(logradouro - bairro - cidade/sigla estado): ')
  endereço = str(input())
  usuario = [nome, dataNascimento, cpf, endereço]
  usuarios.append(usuario) #adicionando o novo usuário à lista
  print('Usuário cadastrado com sucesso!')

def cadastarContaBancaria(usuario): #cadastra a conta bancária
  global numeroConta
  print('Digite o seu CPF: ')
  cpfBuscado = int(input()) #converte para int
  for usuario in usuarios:
    if cpfBuscado == usuario[2]: #busca o cpf na lista de usuários
      numeroContaGlobal = '0001' + '.'+ str(numeroConta)
      usuario.append(numeroContaGlobal)
      numeroConta += 1
      print('Conta bancária cadastrada com sucesso: ', numeroContaGlobal)
      return
    print('CPF não encontrado') 

def listarContas(): #exibe todas contas bancárias criadas
  print("=== Lista de Contas Bancárias ===")
  for i, usuario in enumerate(usuarios, start=1):
    print(f"Usuário: {usuario[0]}")
    print("Contas:")
    for j, conta in enumerate(usuario[4:], start=1):
      print(f"Conta {j}:")
      print(f"Nome: {usuario[0]}")
      print(f"Data de Nascimento: {usuario[1]}")
      print(f"CPF: {usuario[2]}")
      print(f"Endereço: {usuario[3]}")
      print(f"Número da Conta: {conta}")
      print("-" * 30)

main()