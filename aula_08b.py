from math import hypot
cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adjacente = float (input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(cat_oposto,cat_adjacente)
#hipotenusa = (cat_adjacente ** 2 + cat_oposto ** 2) ** (1/2)
print ('A hipotenusa vai medir {:.2f}'.format(hipotenusa))