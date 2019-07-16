print('QUANTIDADE DE TINTA NECESSÁRIA')
l = float(input('Qual é a largura da parede?'))
a = float(input('Qual é a altura da parede?'))
m = l*a
t = m/2
print('A área total a ser pintada é de {}m², portanto será necessário {:.2f} litros de tinta para cobrir'.format(m, t))
print('a área desejada.')

