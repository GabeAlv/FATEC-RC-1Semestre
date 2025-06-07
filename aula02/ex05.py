num1 = int(input('Digite um número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O primeiro número é maior')
elif num2 > num1:
    print(f'O segundo número é maior')
elif num1 == num2:
    print(f'Os dois números são iguais')
