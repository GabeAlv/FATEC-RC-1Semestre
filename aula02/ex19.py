def idade_atleta():
    idade = int(input('Digite a sua idade: '))

    if idade <= 12:
        return 'Infantil'
    elif 17 >= idade >= 13:
        return 'Juvenil'
    elif 40 >= idade >= 18:
        return 'Adulto'
    else:
        return 'Veterano'


print(idade_atleta())
