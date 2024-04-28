class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo #encapsulamento privado
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # regras de depósito
        self._saldo += valor
    
    def sacar(self, valor):
        # regras de saque
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta('0001', 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())