# Projeto 1 Python Básico - BootCamp Python Vivo
# bankSystem.py - Otimizando o Sistema bancário com POO em Python

class Cliente:
  MAX_SAQUES_DIAROS = 3
  VALOR_MAX_SAQUE = 500.00
  NRO_CONTA_GLOBAL = 0

  def __init__(self, nome, cpf, data_de_nascimento, endereco, nro_conta):
      self.nome = nome
      self.cpf = cpf
      self.data_de_nascimento = data_de_nascimento
      self.endereco = endereco
      self.contas_bancarias = []
      self.nro_conta = nro_conta

  def cadastrar_cliente(self): 
      print('Digite o seu nome')
      self.nome = input()
      print('Digite a sua data de nascimento (ex: 20/06/1998): ')
      self.data_de_nascimento = input()
      print('Digite o seu CPF: ')
      self.cpf = input()
      print('Digite o seu endereço (logradouro - bairro - cidade/sigla estado): ')
      self.endereco = input()
      self.contas_bancarias.append([self.nome, self.data_de_nascimento, self.cpf, self.endereco])
      print('Cliente cadastrado com sucesso!')

  def cadastrar_conta_bancaria(self):
      print('Digite o seu CPF: ')
      cpfBusca = input()

      for cliente in self.contas_bancarias:
          if cpfBusca == cliente[2]:
              numero_conta = f'0001.{self.NRO_CONTA_GLOBAL}'
              saldo_inicial = 0
              cliente.extend([numero_conta, saldo_inicial])
              self.NRO_CONTA_GLOBAL += 1
              print('Conta bancária cadastrada com sucesso: ', numero_conta)
              return

      print('CPF não encontrado.')

  def deposito(self, numero_conta, valorDeposito):
      for cliente in self.contas_bancarias:
          if numero_conta in cliente:
              cliente[-1] += valorDeposito  # Adiciona o valor ao saldo
              print(f'Depósito de R${valorDeposito:.2f} realizado com sucesso na conta {numero_conta}')
              return

      print('Conta não encontrada.')

  def saque(self, numero_conta, valorSaque):
      for cliente in self.contas_bancarias:
          if numero_conta in cliente:
              if valorSaque <= cliente[-1]:  # Verifica se há saldo suficiente na conta
                  cliente[-1] -= valorSaque  # Subtrai o valor do saldo
                  print(f'Saque de R${valorSaque:.2f} realizado com sucesso na conta {numero_conta}')
              else:
                  print('Saldo insuficiente para realizar o saque.')
              return

      print('Conta não encontrada.')

  def listar_contas(self):
      for cliente in self.contas_bancarias:
          print(f"=== Contas do cliente {cliente[0]} ===")
          print(f"Nome: {cliente[0]}")
          print(f"Data de Nascimento: {cliente[1]}")
          print(f"CPF: {cliente[2]}")
          print(f"Endereço: {cliente[3]}")
          print(f"Número da Conta: {cliente[-2]}")  # Último elemento é o número da conta
          print(f"Saldo: R${cliente[-1]:.2f}")  # Penúltimo elemento é o saldo
          print("-" * 30)

  def extrato(self, numero_conta):
      for cliente in self.contas_bancarias:
          if numero_conta == cliente[-2]:  # Verifica pelo número da conta
              print(f'=== Extrato da conta {numero_conta} ===')
              print(f'Nome: {cliente[0]}')
              print(f'Data de Nascimento: {cliente[1]}')
              print(f'CPF: {cliente[2]}')
              print(f'Endereço: {cliente[3]}')
              print(f'Número da Conta: {numero_conta}')
              print(f'Saldo: R${cliente[-1]:.2f}')
              return

      print('Conta não encontrada.')

def main():
  cliente = Cliente("", "", "", "", 0)

  while True:
      opcao = show_menu()

      if opcao not in ['d', 's', 'e', 'x', 'c', 'b', 'l']:
          print('Opção inválida!')
          continue

      if opcao == 'd':
          cliente.listar_contas()
          numero_conta = input("Digite o número da Conta: ")
          valorDeposito = float(input('Digite o valor do depósito: '))
          cliente.deposito(numero_conta, valorDeposito)
      elif opcao == 'e':
          cliente.listar_contas()
          numero_conta = input("Número da Conta: ")
          cliente.extrato(numero_conta)
      elif opcao == 's':
          cliente.listar_contas()
          numero_conta = input("Número da Conta: ")
          valorSaque = float(input('Digite o valor do saque: '))
          cliente.saque(numero_conta, valorSaque)
      elif opcao == 'c':
          cliente.cadastrar_cliente()
      elif opcao == 'b':
          cliente.cadastrar_conta_bancaria()
      elif opcao == 'l':
          cliente.listar_contas()
      elif opcao == 'x':
          break

def show_menu():
  MENU = '''
============MENU============
|                          |
| d = Depósito             |
| c = cadastrar cliente    |
| b = cadastrar conta banc |
| s = Saque                |
| e = Extrato              |
| l = Listar contas        |
| x = Sair                 |
|                          |
===========================
'''
  print(MENU + '\nOpção: ')
  opcao = input().lower()
  return opcao

if __name__ == "__main__":
  main()
