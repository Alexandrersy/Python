valores=[]
for i in range(int(input('Digite a quantidade de valores: '))):
    valores.append(float(input('Digite os valores: ')))
valores.sort()
print(valores)

print('O menor valor da lista é ',min(valores))