print('='*10+'Calculadora de tarifas de ônibus'+'='*10)
idade = int(input('Qual a sua idade? '))
cartao_estudante = input('''Você tem o seu cartão de estudante?
Sim (se você tiver)
Não (se você não tiver)
Resposta: ''').lower()
print('  ')
if idade < 6 or idade > 65:
    print('--->Você tem tarifa grátis<---')
elif cartao_estudante == 'sim':
    print('--->Você tem 50% de desconto<---')
else:
    print('--->Você paga a tarifa normal<---')
