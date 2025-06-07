print('='*6+'Cálculo de imposto de renda'+'='*6)
salario = float(input('Qual o seu sálario bruto? '))

if salario <= 1900:
    print('Você está isento do imposto de renda')
elif 2800 >= salario > 1900:
    taxa = salario * 0.075
    print('Você pagará uma taxa de 7.5%')
    print(f'Que será R${taxa:.2f}')
elif 3700 >= salario > 2800:
    taxa = salario * 0.15
    print('Você pagará uma taxa de 15%')
    print(f'Que será R${taxa:.2f}')
elif 4600 >= salario > 3700:
    taxa = salario * 0.225
    print('Você pagará uma taxa de 22.5%')
    print(f'Que será R${taxa:.2f}')
elif salario > 4600:
    taxa = salario * 0.275
    print('Você pagará uma taxa de 27.5%')
    print(f'Que será R${taxa:.2f}')
