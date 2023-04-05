from Pessoa import Pessoa
from Fisica import Fisica


class Juridica(Pessoa):
    def __init__(self, nome, fone, cidade, cnpj):
        super().__init__( nome, fone, cidade)
        self.cnpj = cnpj
        self.qtd_funcionarios = 0
        self.funcionarios = []
    
    def addFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)
        self.qtd_funcionarios += 1

    def imprimir(self):
        print("Empresa: ", self.nome)
        print("Fone: ", self.fone)
        print("Cidade :", self.cidade.nome)
        print("Qtd funcionários: ", self.qtd_funcionarios)
        print("Funcionários: \n-------")
        if len(self.funcionarios) > 0:
            for func in self.funcionarios:
                print("Nome Funcionario: ", func.nome)
                print("Fone Funcionario: ", func.fone)
                print("Cidade Funcionario: ", func.cidade.nome)
                print("-------")