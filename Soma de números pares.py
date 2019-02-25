from time import sleep
print(30*'=')
print('Ex050 - SOMANDO NÚMEROS PARES')
print(30*'=')
tpar = 0
spar = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número inteiro: '.format(c)))
    print(30*'-')
    if n % 2 == 0:
        tpar += 1
        spar += n
print('')
print('Imprimindo resultado...')
sleep(1)
print(48*'=')
if tpar == 0:
    print('Não foi digitado nenhum número par. [ Soma = {} ]'.format(spar))
elif tpar == 1:
    print('Foi digitado apenas {} número par. [ Soma = {} ]'.format(tpar, spar))
else:
    print('Foram digitados {} números pares. [ Soma = {} ]'.format(tpar, spar))
print(48*'=')