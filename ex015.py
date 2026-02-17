from math import sqrt

km = float(input('Quantos km percorridos? '))
dias = int(input('Quantos dias o carro foi alugado? '))

preco_por_dia = 60.0
preco_por_km = 0.15

valor_total = preco_por_dia * dias + preco_por_km * km

print('Preço a pagar: R${:.2f}'.format(valor_total))
print(sqrt(144))