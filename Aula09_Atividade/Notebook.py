from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria
    
    def getInformacoes(self):
        print(f"Tempo de bateria: {self.__tempoDeBateria} horas")
        return super().getInformacoes()

    def cadastrar(self):
        print('Seu Notebook foi Cadastrado!')