num = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
resultado = num + num2
print('A soma entre {} e {} vale {}'.format(num, num2, resultado))

if resultado > 10:
    print('Resultado é maior que 10')
else:
    print('resultado menor ou igual a 10')

