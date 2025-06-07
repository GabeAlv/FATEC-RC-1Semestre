import random

usuario = int(input('Advinhe o número de 0 a 10: '))
numero_aleatorio = random.randint(0, 10)

if usuario > numero_aleatorio:
    print('Muito alto')
    print(f'O número secreto era {numero_aleatorio}')
elif usuario < numero_aleatorio:
    print('Muito baixo')
    print(f'O número secreto era {numero_aleatorio}')
elif usuario == numero_aleatorio:
    print('Parabéns você acertou!!')
    print(f'O número secreto é {numero_aleatorio}, igual ao seu ')
