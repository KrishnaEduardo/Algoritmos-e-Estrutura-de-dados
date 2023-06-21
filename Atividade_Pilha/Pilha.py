from No import No

class Pilha:
    def __init__(self):
        self.inicio = None
        self.topo = None
        self.tamanho = 0
    
    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
            self.topo = nodo
        else:
            self.topo.proximo = nodo
            nodo.anterior = self.topo
            self.topo = nodo
        self.tamanho += 1
        self.imprimir()   
        
    def imprimir(self):
        print("---------------------")
        texto = ""
        if self.inicio == None:
            texto = "Pilha Vazia!"
        else:
            aux = self.inicio
            while aux :
                texto += str(aux.dado) + " - "
                aux = aux.proximo
            print( "Tamanho: ", str(self.tamanho))
        print( texto )
                    
    def remover(self):
        if self.inicio == None:
            print("Pilha Vazia!")
            return
        elif self.inicio.proximo == None:
            self.inicio = None
            self.topo = None
            self.tamanho = 0
        else:
            self.topo = self.topo.anterior
            self.topo.proximo = None
            self.tamanho -= 1
        self.imprimir()         