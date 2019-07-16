print('DESCONTO')
p = int(input('Qual o preço do produto?'))
d = int(input('Quanto de desconto será dado?'))
de = (d*p)/100
f = p-de
print('O preço do produto com {}% de desconto fica por {} reais.'.format(d, f))


