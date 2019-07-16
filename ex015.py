print('ALUGUEL DE CARRO:')
d = float(input('Dias utilizados:'))
k = float(input('Kilomêtros rodados:'))
p = (d*60)+(k*0.15)
print('O valor a ser pago pelo aluguel do carro é de R${:.2f}'.format(p))


