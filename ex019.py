from random import choice

# students = [
#     input('Informe o nome do aluno 1: '),
#     input('Informe o nome do aluno 2: '),
#     input('Informe o nome do aluno 3: '),
# ]

students = []
for i in range(1, 5):
    students.append(input('Informe o nome do aluno {}: '.format(i)))

print('O aluno sorteado para apagar o quadro é {}: '.format(choice(students)))