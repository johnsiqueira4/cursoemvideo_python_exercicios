money = float(input('Informe seu saldo R$: '))
cotacao = 3.27
print('Você pode comprar ${:.2f} dólares e sobram R${:.2f} reais'.format(money//cotacao, money%cotacao))