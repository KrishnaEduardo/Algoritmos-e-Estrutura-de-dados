from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook


d = Desktop('PC', 'Branco', 12000, 750)
d.getInformacoes()
d.cadastrar()

print('-----------------')

n = Notebook('AIR M1', 'Prata', 8000, 18)
n.getInformacoes()
n.cadastrar()