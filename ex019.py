import random
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo Aluno'))
n3 = str(input('Terceiro Aluno'))
n4 = str(input('Quarto luno'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))







