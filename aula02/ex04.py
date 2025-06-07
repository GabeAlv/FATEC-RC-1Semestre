idade = int(input('Qual a sua idade? '))

if idade < 12 or idade > 60:
    print(f'Você tem {idade} anos, portanto irá pagar 15 reais de ingresso')
else:
    print(f'Você tem {idade} anos, portanto pagará 30 reais de ingresso')
