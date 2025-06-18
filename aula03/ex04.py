'''
Caixa eletrônico
'''
valor = int(input('Digite um valor inteiro: '))
lista = [100, 50, 20, 10, 5, 2, 1]
tabela_notas = {}

for i in range(7):
    tabela_notas[lista[i]] = valor // lista[i]
    valor = valor % lista[i]

print(tabela_notas)
