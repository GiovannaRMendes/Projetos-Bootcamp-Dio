import re

from abc import ABC, abstractmethod
from datetime import datetime, date


class Historico():
    def __init__(self):
        self._transacoes = []

    
    @property
    def transacoes(self):
        return self._transacoes


    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        )


class Transacao(ABC):
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
    

    @property
    def valor(self):
        return self._valor
    

    def registrar(self, conta):

        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    
    @property
    def valor(self):
        return self._valor
    

    def registrar(self, conta):

        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


class Conta():
    def __init__(self, numero: int, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    

    @property
    def cliente(self) -> float:
        return self._cliente
    

    @property
    def historico(self) -> float:
        return self._historico


    @property
    def saldo(self) -> float:
        return self._saldo
    

    @property
    def numero(self) -> float:
        return self._numero
    

    @property
    def agencia(self) -> float:
        return self._agencia
    

    def depositar(self, valor: float) -> bool:

        if valor > 0:
            self._saldo += valor
            return True
        
        print("Não foi possível continuar com a operação. Valor informado está incorreto para depósito!")
        return False
    

    def sacar(self, valor: float) -> bool:

        if self.saldo >= valor and valor > 0:
            self._saldo -= valor
            return True

        elif self.saldo < valor:
            print("Não foi possível continuar com a operação. Valor a ser sacado é maior que o saldo!")

        else:
            print("Não foi possível continuar com a operação. Valor informado para saque é inferior ou igual a zero!")
        
        return False


    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(numero, cliente)


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente, limite: float, limite_saques: int):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self) -> int:
        return self._limite
    
    
    @property
    def limite_saques(self) -> int:
        return self._limite_saques


    def sacar(self, valor: float) -> bool:

        numero_saques = len([transacao for transacao in self._historico.transacoes if transacao['tipo'] == Saque.__name__])

        if numero_saques < self.limite_saques and valor <= self.limite:
            return super().sacar(valor)
        
        elif numero_saques >= self.limite_saques:
            print("Não foi possível continuar com a operação. O número de saques diários foi ultrapassado!")

        elif valor >= self.limite:
            print("Não foi possível continuar com a operação. Valor informado é superior ao limite!")

        return False


class Cliente():
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas = []


    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)


    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: date):
        super().__init__(endereco)
        self._cpf = re.sub(r'\D', '', cpf)
        self._nome = nome
        self._data_nascimento = data_nascimento
