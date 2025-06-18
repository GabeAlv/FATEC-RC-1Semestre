'''
Cálculo do fatorial
'''
numero = int(input('Digite um número inteiro positivo: '))

#Usando for
fatorial = 1
for i in range(1, numero+1):
    fatorial = fatorial * i
print(f'(For) O fatorial de {numero}! é {fatorial}')

#Usando while
print(' ')

fatorial2 = 1
x2 = 1
x3 = numero
while x2 <= x3:
    fatorial2 = fatorial2 * numero
    numero = numero - 1
    x2 = x2 + 1
print(f'(While) O fatorial de {x3}! é {fatorial2}')
