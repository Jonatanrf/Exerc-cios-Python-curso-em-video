print('AUMENTO DE SALÁRIO')
n = input('Qual o nome do funcionário?')
s = float(input('Salário do funcionário:R$'))
a = float(input('quanto de aumento será dado?'))
au = (s*a)/100
f = s+au
print('Com o aumento de {}%, o salário de {} ficará {} reais'.format(a, n, f))

