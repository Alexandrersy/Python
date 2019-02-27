valores=[]
for i in range(int(input('Digite a quantidade de valores: '))):
    valores.append(int(input('Digite os valores: ')))
valores.sort()
print(valores)

print('Maior valor: '.format(max(valores)))
print('Menor valor: '.format(min(valores)))

print('A diferença entre o maior e o menor número é: ', min(valores)-max(valores))