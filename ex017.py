import math
cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

# hipotenusa = math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2)
# hipotenusa = math.sqrt(hipotenusa)
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('Hipotenusa: {:.2f}'.format(hipotenusa))