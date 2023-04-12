from Fisica import Fisica
from Pessoa import Pessoa
from Cidade import Cidade
from Juridica import Juridica

c1 = Cidade(1, "Porto Alegre")
c2 = Cidade(1, "São Paulo")

pf1 = Fisica("João", "123456", c1, "000.222")
p1  = Pessoa("Marcela", "95854", c2)
#pf1.imprimir()

print(p1)
print("-------------------------")
print(pf1)
