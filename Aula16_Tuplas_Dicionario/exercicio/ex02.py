nome = input("Digite seu nome: ")
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

aluno = {
    "nome: " : nome,
    "nota01" : n1,
    "nota02" : n2
}

nf = (n1+n2)/2
aluno["notaFinal"] = nf
print(aluno)