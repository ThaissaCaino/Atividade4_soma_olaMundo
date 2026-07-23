import math

an = float(input('digite o ângulo: '))
seno = math.sin(math.radians(an))

print('o angulo {} tem seno de {:.2f}'.format(an,seno))

cosseno = math.cos(math.radians(an))
print('O ângulo {} tem cosseno de {:.2f}.'.format(an,cosseno))
tangente = math.tan(math.radians(an))
print(('O ângulo {} tem tangente de {:.2f}.'.format(an,tangente)))