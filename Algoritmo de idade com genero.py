idade=int(input('Digite a sua idade: '))
sexo=input('Digite seu sexo com M ou F: ')

if idade <18 and sexo =='m':
    print('Homem menor de idade')
elif idade >=18 and sexo =='m':
    print('Homem maior de idade')
elif idade <18 and sexo =='f':
    print('Mulher menor de idade')
elif idade >=18 and sexo =='f':
    print ('Mulher maior de idade')
else:
    print('Erro na entrada de dados')