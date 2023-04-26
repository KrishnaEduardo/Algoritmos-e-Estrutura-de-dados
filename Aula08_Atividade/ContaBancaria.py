from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, saldo=None):
        self.saldo = saldo