class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print('CC N°: %s Saldo: %10.2f' % (self.numero, self.saldo))
        print('Titular: %s Telefone: %s' % (self.clientes[0].nome, self.clientes[0].telefone))
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque', valor])
        else:
            print('Saldo insuficiente')
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['Depósito', valor])
    def extrato(self):
        print('Extrato CC N°: %s' % self.numero)
        for o in self.operacoes:
            print('%10s %10.2f' % (o[0], o[1]))
        print('Saldo: %10.2f' % self.saldo)