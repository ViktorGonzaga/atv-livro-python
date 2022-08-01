from clientes import Cliente
from contas import Conta

joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")
jose = Cliente("José da Silva", "444-1234")

conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria], 2, 2000)
conta3 = Conta([joao, jose], 3, 500)