peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / pow(altura, 2)

print(f'Seu imc é {imc:.2f}')
if imc < 18.5:
    print(f'Você está abaixo do peso')
elif 24.9 > imc > 18.5:
    print(f'Você está no peso normal')
elif 29.9 > imc > 25:
    print(f'Você está com sobrepeso')
elif 39.9 > imc > 30:
    print(f'Você está com obesidade CUIDADO!!')
else:
    print(f'OBESIDADE GRAVE')
