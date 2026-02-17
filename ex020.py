from encodings import search_function
from random import shuffle

alunos = []
for i in range(1, 5):
    alunos.append(input('Digite o nome do aluno {}: '.format(i)))

# alunos_ordem = sorted(alunos, key=alunos.index, reverse=True)
# print('alunos: ', alunos)
# print('alunos_ordem: ', alunos_ordem)

# primeiro = choice(alunos)
#
# segundo = choice(alunos)
# while segundo == primeiro:
#     segundo = choice(alunos)
#
# terceiro = choice(alunos)
# while terceiro == primeiro or terceiro == segundo:
#     terceiro = choice(alunos)
#
# quarto = choice(alunos)
# while quarto == terceiro or quarto == segundo or quarto == primeiro:
#     quarto = choice(alunos)


# primeiro = choice(alunos)
# alunos.remove(primeiro)
# segundo = choice(alunos)
# alunos.remove(segundo)
# terceiro = choice(alunos)
# alunos.remove(terceiro)
#
# print('Ordem apresentação: {}, {}, {}, {}.'.format(primeiro, segundo, terceiro, alunos[0]))

shuffle(alunos)
print('Ordem de apresentação: ', alunos)