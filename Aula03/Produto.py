class Produto:
    def __init__(self, nome, preco, categoria):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.cat = categoria
    
    def imprimir(self):
        print("----------------------")
        print("Nome:", self.nome)
        print("Preço:", self.preco)
        print("Produto:", self.cat.nome)