print('CÁLCULO DE SENO COSSENO E TANGENTE.')
from math import sin, cos, tan,radians
a = int(input('Digite o ângulo:'))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('Referente ao ângulo {}, seu seno é {:.2f}, cosseno é {:.2f}\ne sua tangente é {:.2f}'.format(a, s, c, t))
