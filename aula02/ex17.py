valor_saque = float(input('Digite o valor do saque: '))
notas = [100, 50, 20, 10]

tabela_notas = {}
for x in range(4):
    tabela_notas[notas[x]] = valor_saque // notas[x]
    valor_saque = valor_saque % notas[x]

print(tabela_notas)
