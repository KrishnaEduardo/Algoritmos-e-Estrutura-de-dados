from ContaBancaria import ContaBancaria

class Corrente(ContaBancaria):
    def __init__(self, saldo=None):
        super().__init__(saldo)