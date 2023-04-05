from Cidade import Cidade
from Pessoa import Pessoa

from Produto import Produto
from Pedido import Pedido
from Categoria import Categoria

poa = Cidade(1, "Porto Alegre")
p1 = Pessoa("João", "3344-5566", poa)
p2 = Pessoa("Maria", "2233-4455", poa)
#print("Nome da cidade da", p2.nome,"é", p2.cidade.nome )
#p1.imprimir()

print("---29/03/2003---")
cat1 = Categoria(1, "Bebidas")
cat2 = Categoria(2, "Alimentos")

prod1 = Produto("Coca-Cola", 7.99, cat1)
prod2 = Produto("Fanta", 6.95, cat1)
prod3 = Produto("Arroz", 3.99, cat2)

pedi01 = Pedido("Rua a, 100", p2)
pedi01.imprimir()

print("Soma do Pedido: ", pedi01.addProduto(prod1))
print("Soma do Pedido: ", pedi01.addProduto(prod3))
print("----------")
pedi01.imprimir() 