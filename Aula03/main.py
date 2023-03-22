from Cidade import Cidade
from Pessoa import Pessoa


poa = Cidade(1, "Porto Alegre")
p1 = Pessoa("João", "3344-5566", poa)
p2 = Pessoa("Maria", "2233-4455", poa)
print("Nome da cidade da", p2.nome,"é", p2.cidade.nome )