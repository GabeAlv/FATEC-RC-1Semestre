temperatura = float(input('Qual a temperatura em Celsius? '))

if temperatura <= 15:
    print('Frio')
elif 25 >= temperatura >= 16:
    print('Agradável')
elif temperatura > 25:
    print('Quente')
