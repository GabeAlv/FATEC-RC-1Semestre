preco_original = float(input('Qual é o preço do produto? '))
desconto = float(input('Qual o desconto do produto? '))
preco_final = preco_original - (preco_original * (desconto / 100))

print(f'O produto que custava R${preco_original} com desconto de {desconto:.0f}% vai custar agora R${preco_final:.2f}')

