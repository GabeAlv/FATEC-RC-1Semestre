def simulacao_fila():
    idade = int(input('Digite a sua idade: '))
    gestante = input('Você é gestante? [S/N] ').upper()
    deficiente = input('Você é deficiente? [S/N] ').upper

    if idade >= 60 or deficiente == 'S':
        return 'Prioridade máxima'
    elif gestante == 'S':
        return 'Prioridade média'
    else:
        return 'Atendimento normal'


print(simulacao_fila())
