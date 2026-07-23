import random
n1 = str(input('Nome do 1º aluno: '))
n2 = str(input('2º aluno: '))
n3 = str(input('3º aluno: '))
n4 = str(input('4º aluno: '))
lista = [n1,n2,n3,n4]

escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

