class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome 
        self.matricula = matricula 
    
    def imprimir(self):
        print("Codigo: ", self.codigo)
        print("Nome: ", self.nome)
        print("Matricula: ", self.matricula)

class AluEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano
    
    def imprimir(self):
        print("Codigo: ", self.codigo)
        print("Nome: ", self.nome)
        print("Matricula: ", self.matricula)
        print("Ano: ", self.ano)


#aluno = Aluno(14, "João", 5454)
#aluno.imprimir()

aluno1 = AluEnsinoMedio("14", "João", "5454", "123")
aluno1.imprimir()