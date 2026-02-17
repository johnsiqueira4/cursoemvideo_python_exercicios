largura = float(input('Qual a largura da parede em metros? '))
altura = float(input('Qual a altura da parede em metros? '))

area = largura * altura

rendimento = 2

litros_tinta = area / rendimento
print('Sua parede tem a dimensão de {:.2f}x{:.2f}, e tem area de {:.3f}'.format(largura, altura, area))
print('A quantidade de tinta necessária é {:.4f} litros'.format(litros_tinta))