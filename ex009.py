num = input('Digite um numero inteiro: ')

while not num.isnumeric():
    num = input('Digite um numero >inteiro<:')

num = int(num)
print('-' * 12)
for i in range(1, 11):
    print('{} X {:0>2} = {:0>2}'.format(num, i, num*i))
print('-' * 12)