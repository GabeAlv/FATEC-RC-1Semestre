def sistema_login_simples():
    x = 1
    while True:
        usuario = input('Digite o seu usuario: ')
        senha = input('Digite a sua senha: ')

        if usuario == 'gabriel' and senha == '12345abc':
            print('Login bem-sucedido')
            break
        elif x == 3:
            print('Acesso Bloqueado')
            break
        else:
            print('Usuário ou senha incorretos')
        x += 1

sistema_login_simples()
