print('TEOREMA DE PITAGORAS(comprimento da hipotenusa')
from math import hypot
co = float(input('comprimento do cateto hoposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(ca, co)
print('A hipotenusa vai medir {:.2f}!'.format(hi))
