from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte
    
    def getInformacoes(self):
        print(f"Potência da Fonte: {self._potenciaDaFonte} W")
        return super().getInformacoes()
    
    def cadastrar(self):
        print('Seu Desktop foi Cadastrado!')