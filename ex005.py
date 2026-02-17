num = input('Digite um numero inteiro: ')

while not num.isnumeric():
    num = input('Digite um numero >inteiro<: ')

print('Sucessor: {}'.format(int(num) + 1))
print('Antecessor: {}'.format(int(num) - 1))