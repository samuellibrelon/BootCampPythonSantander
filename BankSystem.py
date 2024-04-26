# Projeto 1 Python Básico - BootCamp Python Vivo
# BankSystem - Sistema bancário 

QTD_SAQUE = 3
QTD_DEPOSITO = 0
saldo = 1000.00

def main():
  while True:
    opcao = showMenu()
    if opcao not in ['d', 's', 'e', 'x']: #verifica input
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
  if QTD_SAQUE > 0: #verifica se excedeu o valor máximo de saques
    if  0 < valorSaque <= 500.00: #verifica se é um valor entre 0 e 501
      saldo -= valorSaque
      QTD_SAQUE -= 1
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
  =======MENU=======
  |                  |
  | d = Depósito     |
  | s = Saque        |
  | e = Extrato      |
  | x = sair         |
  |                  |
  ==================
  '''
  print (MENU + '\nOpção: ')
  opcao = str(input().lower())
  return opcao

main()
