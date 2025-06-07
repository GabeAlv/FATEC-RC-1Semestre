valor_compra = float(input('Qual o valor da compra? R$ ').replace(',' ,'.'))

if valor_compra > 100:
    print(f'Você tem frete gratis')
elif valor_compra <= 100:
    print(f'Você não tem frete gratis, pelo produto não ser acima de R$100')
