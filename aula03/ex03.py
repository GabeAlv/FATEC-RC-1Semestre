'''
Soma de números pares
'''

#usando for
numero = int(input('Digite um número por favor: '))
soma = 0
for i in range(1,numero+2):
    if i % 2 == 0:
        soma = soma + i
print(f'(Com for) A soma dos números pares de 1 até {numero} é {soma}')

print('')

#usando while
numero1 = int(input('Digite um número: '))
x = 2
soma2 = 0
while x <= numero1:
    soma2 = soma2 + x
    x = x + 2
print(f'(Com while) A soma dos números pares de 1 até {numero1} é {soma2}')
