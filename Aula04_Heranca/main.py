from Fisica import Fisica
from Pessoa import Pessoa
from Cidade import Cidade
from Juridica import Juridica

c1 = Cidade(1, "Porto Alegre")
c2 = Cidade(1, "São Paulo")

joao = Fisica("João", "2233-4455", c1, "000.111.222-33")
maria = Fisica("Maria", "9988-7766", c2, "606.601.016-96")
jose = Fisica("José", "9988-7766", c2, "333.303.888-48")

dosul = Juridica("Supermercado DoSul", "234-4321", c1, "01.234.567/0001-00")


dosul.imprimir()
dosul.addFuncionario(joao)
dosul.addFuncionario(maria)

print("--------\n\n")
dosul.imprimir()
