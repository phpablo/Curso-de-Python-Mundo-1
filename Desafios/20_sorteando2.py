import random

# Lista com os nomes dos alunos
alunos = ['Alice', 'Bob', 'Carol', 'David']

# Embaralha a ordem dos alunos
random.shuffle(alunos)

# Mostra na tela a ordem sorteada de apresentação dos trabalhos
print("Ordem de apresentação dos trabalhos:")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")
