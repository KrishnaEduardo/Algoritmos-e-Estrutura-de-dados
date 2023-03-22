class Pessoa_: 
    
    idade = None

    def __init__(self, nome, idade):
        print("Objeto instanciado")
        #self.nome = "Maria"
        self.nome = nome 
        self.idade = idade
        self.fone = input("Digite seu fone: ")

    def imprimir(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Telefone: ", self.fone)