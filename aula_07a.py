#print('='*20 + ' Desafio nº 5 ' + '='*20)
#n = int(input('Digite um número para saber seu antecessor e sucessor: '))
#ant = n - 1
#suce = n + 1

#print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, ant, suce))
#print(('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1))))

#print('='*20 + ' Desafio nº 6 ' + '='*20)
#n2 = int(input('Digite o número para dobro, triplo e raiz quadrada: '))
#print('O dobro de {} vale {} \nO triplo de {} vale {} \nA raiz quadrada de {} é igual a {:.2f}'.format(n2, (n2*2), n2, (n2*3), n2, (n2**(1/2))))

#print('='*20 + ' Desafio nº 7 ' + '='*20)
#nota1 = float(input('Primeira nota do aluno: '))
#nota2 = float(input('Segunda nota do aluno: '))
#media = (nota1 + nota2) / 2
#print('A média entre {} e {} é {}'.format(nota1, nota2, ((nota1 + nota2)/2)))
#print('A média entre {:.1f} e {:.1f} é {:.1f}'.format(nota1, nota2, media))

'''print('*' * 10, ' Desafio nº 8 ', '*' * 10)
medida = float(input('Digite uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {:.3f} metros corresponde a\n{:.3f} km;\n{:.3f} hm;\n{:.3f} dam;\n{:.3f} dm;\n{:.3f} cm;\n{:.3f} mm.'.format(medida, km, hm, dam, dm, cm, mm))
'''

'''print('#'*15, ' Desafio nº 9 ', '#'*15)
num = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    resultado = num * i
    print('{} * {} = {}'.format(num, i, resultado))'''

'''print('S2'*15, ' Desafio nº 10 ', 'S2'*15)
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = float(input('Digite o valor do dólar: US$ '))
compra = real / dolar
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, compra))'''

'''print('#'*15, ' Desafio nº 11 ', '#'*15)
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área de é de {}m².'.format(larg,alt,area))
tinta = area / 2
print('Para pintar a parede vai precisar de {} litros de tinta.'.format(tinta))'''

'''
print('#'*15, ' Desafio nº 12 ', '#'*15)
preco = float(input('Qual o preço do produto? R$'))
novo = preco - (preco * 5/100)
print('O preço com desconto é R${:.2f}'.format(novo))
'''

'''
print('#' * 15, ' Desafio nº 13 ', '#' * 15)
salario = float(input('O salário atual é: R$'))
novo = salario + (salario * 15/100)
print('O novo salário com aumento de 15% é de R${:.2f}'.format(novo))
'''

'''
print('#' * 15, ' Desafio nº 14 ', '#' * 15)
temp_c = float(input('Digite a temperatura em °C: '))
temp_f = 9 * temp_c / 5 + 32
print('A conversão da temperatura {:.2f}°C em °F é {:.2f}.'.format(temp_c,temp_f))
'''

print('#' * 15, ' Desafio nº 15 ', '#' * 15)
dia = int(input('Entre com a quantidade de dias de aluguel: '))
km = float(input('Entre com a quantidade de km percorrido: '))
pago = dia * 60 + km * 0.15
print(pago)
