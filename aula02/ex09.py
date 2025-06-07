salario = float(input('Qual o seu salário? '))

if salario < 2000:
    bonus = salario * 0.20
    print(f'Seu salário é R${salario} portanto terá um bônus de 20%')
    print(f'O acréscimo com seu salário ficará R${salario + bonus:.2f}')
elif 5000 > salario >= 2000:
    bonus = salario * 0.10
    print(f'Seu salário é R${salario} portanto terá um bônus de 10%')
    print(f'O acréscimo com seu salário ficará R${salario + bonus:.2f}')
elif salario >= 5000:
    bonus = salario * 0.05
    print(f'Seu salário é R${salario} portanto terá um bônus de 5%')
    print(f'O acréscimo com seu salário ficará R${salario + bonus:.2f}')
